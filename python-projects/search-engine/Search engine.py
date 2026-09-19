import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext, font
from fuzzywuzzy import fuzz
from typing import List, Tuple, Dict, Set
import string
import re
from collections import Counter
import math

class SmartSearchEngine:
    def __init__(self):
        self.document_store: Dict[int, str] = {}
        self.doc_id_counter = 0
        self.word_frequency: Dict[str, Counter] = {}
        self.total_documents = 0
        
    def _tokenize(self, text: str) -> List[str]:
        """Convert text into tokens, handling various cases."""
        # Convert to lowercase and remove punctuation
        text = text.lower()
        text = text.translate(str.maketrans("", "", string.punctuation))
        
        # Split into words
        words = text.split()
        
        # Generate variations for each word
        tokens = set()
        for word in words:
            tokens.add(word)
            # Add common variations
            tokens.add(self._remove_repeated_chars(word))
            tokens.update(self._generate_phonetic_variations(word))
        
        return list(tokens)
    
    def _remove_repeated_chars(self, word: str) -> str:
        """Remove repeated characters (e.g., 'gooogle' -> 'google')."""
        return re.sub(r'(.)\1+', r'\1\1', word)
    
    def _generate_phonetic_variations(self, word: str) -> Set[str]:
        """Generate common phonetic and spelling variations."""
        variations = set()
        
        # Common letter substitutions
        substitutions = {
            'ph': 'f', 'f': 'ph',
            'ai': 'ay', 'ay': 'ai',
            'ie': 'ei', 'ei': 'ie',
            'oo': 'u', 'u': 'oo',
            'ks': 'x', 'x': 'ks',
            'shun': 'tion', 'tion': 'shun'
        }
        
        # Generate variations using substitutions
        for old, new in substitutions.items():
            if old in word:
                variations.add(word.replace(old, new))
        
        # Handle common prefixes and suffixes
        if word.endswith('y'):
            variations.add(word[:-1] + 'ie')
            variations.add(word[:-1] + 'ies')
        if word.endswith('ing'):
            variations.add(word[:-3])
            variations.add(word[:-3] + 'e')
        
        return variations
    
    def add_document(self, text: str) -> int:
        """Add a document and update the search index."""
        doc_id = self.doc_id_counter
        self.document_store[doc_id] = text
        
        # Update word frequency index
        tokens = self._tokenize(text)
        if doc_id not in self.word_frequency:
            self.word_frequency[doc_id] = Counter(tokens)
        
        self.doc_id_counter += 1
        self.total_documents += 1
        return doc_id
    
    def _calculate_tf_idf(self, term: str, doc_id: int) -> float:
        """Calculate TF-IDF score for term in document."""
        # Term frequency in document
        tf = self.word_frequency[doc_id][term]
        
        # Inverse document frequency
        docs_with_term = sum(1 for doc_freq in self.word_frequency.values() if term in doc_freq)
        idf = math.log((self.total_documents + 1) / (docs_with_term + 1)) + 1
        
        return tf * idf
    
    def _calculate_similarity_score(self, query_tokens: List[str], doc_id: int) -> float:
        """Calculate document similarity score using multiple factors."""
        doc_text = self.document_store[doc_id].lower()
        score = 0.0
        
        for token in query_tokens:
            # TF-IDF score
            tf_idf = self._calculate_tf_idf(token, doc_id)
            
            # Fuzzy string matching
            best_fuzzy_score = 0
            for doc_token in self._tokenize(doc_text):
                fuzzy_score = fuzz.ratio(token, doc_token) / 100.0
                best_fuzzy_score = max(best_fuzzy_score, fuzzy_score)
            
            # Combine scores
            token_score = (tf_idf * 0.6) + (best_fuzzy_score * 0.4)
            score += token_score
        
        return score / len(query_tokens)
    
    def search(self, query: str, threshold: float = 0.3) -> List[Tuple[int, str, float, List]]:
        """Perform Google-style search with spelling correction."""
        # Tokenize query
        query_tokens = self._tokenize(query)
        results = []
        
        for doc_id in self.document_store:
            # Calculate relevance score
            score = self._calculate_similarity_score(query_tokens, doc_id)
            
            if score >= threshold:
                # Find matching terms for highlighting
                matches_info = []
                doc_tokens = self._tokenize(self.document_store[doc_id])
                
                for q_token in query_tokens:
                    best_match = None
                    best_score = 0
                    
                    for d_token in doc_tokens:
                        match_score = fuzz.ratio(q_token, d_token) / 100.0
                        if match_score > best_score:
                            best_score = match_score
                            best_match = d_token
                    
                    if best_match and best_score >= threshold:
                        matches_info.append((q_token, best_match, best_score))
                
                results.append((doc_id, self.document_store[doc_id], score, matches_info))
        
        # Sort by relevance score
        return sorted(results, key=lambda x: x[2], reverse=True)

class SearchEngineGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Search Engine")
        self.root.geometry("800x600")
        
        # Initialize styles and GUI
        self.search_engine = SmartSearchEngine()
        self.current_results = []
        self.current_result_index = 0
        self.setup_gui()

    def setup_gui(self):
        # Main container with padding
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Header section with file selection
        header_frame = ttk.Frame(main_frame)
        header_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15))
        
        self.file_label = ttk.Label(header_frame, text="No file selected", font=("Arial", 10))
        self.file_label.grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        
        select_button = ttk.Button(header_frame, text="Select File", command=self.select_file)
        select_button.grid(row=0, column=1)
        
        # Search section
        search_frame = ttk.Frame(main_frame)
        search_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15))
        
        ttk.Label(search_frame, text="Search:", font=("Arial", 10, "bold")).grid(
            row=0, column=0, padx=(0, 10))
        
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(search_frame, textvariable=self.search_var, width=50)
        self.search_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        
        search_button = ttk.Button(search_frame, text="Search", command=self.perform_search)
        search_button.grid(row=0, column=2)
        
        # Navigation section
        nav_frame = ttk.Frame(main_frame)
        nav_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))
        
        self.prev_button = ttk.Button(nav_frame, text="◀ Previous", command=self.show_previous_result, state=tk.DISABLED)
        self.prev_button.grid(row=0, column=0, padx=(0, 10))
        
        self.result_label = ttk.Label(nav_frame, text="")
        self.result_label.grid(row=0, column=1, padx=(10, 10))
        
        self.next_button = ttk.Button(nav_frame, text="Next ▶", command=self.show_next_result, state=tk.DISABLED)
        self.next_button.grid(row=0, column=2, padx=(10, 0))
        
        # Results area
        self.results_text = scrolledtext.ScrolledText(
            main_frame, width=80, height=30, font=("Arial", 10))
        self.results_text.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure text tags for highlighting
        self.results_text.tag_configure("match", background="#fff2cc", foreground="#000000")
        self.results_text.tag_configure("score", foreground="#0066cc", font="Arial 10 bold")
        self.results_text.tag_configure("header", foreground="#444444", font="Arial 11 bold")
        self.results_text.tag_configure("separator", foreground="#cccccc")
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)
        search_frame.columnconfigure(1, weight=1)
        
        # Bind Enter key to search
        self.search_entry.bind('<Return>', lambda e: self.perform_search())

    def select_file(self):
        """Handle file selection and loading."""
        file_path = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                self.search_engine = SmartSearchEngine()
                self.search_engine.add_document(content)
                self.file_label.config(text=f"File: {file_path.split('/')[-1]}")
                self.results_text.delete('1.0', tk.END)
                self.results_text.insert(tk.END, "File loaded successfully. Enter a search term above.", "header")
                # Reset navigation
                self.current_results = []
                self.current_result_index = 0
                self.update_navigation_buttons()
            except Exception as e:
                self.results_text.delete('1.0', tk.END)
                self.results_text.insert(tk.END, f"Error loading file: {str(e)}", "header")

    def find_match_in_context(self, text: str, term: str, context_chars: int = 100) -> str:
        """Find the term in text and return the surrounding context with the term highlighted."""
        text_lower = text.lower()
        term_lower = term.lower()
        
        index = text_lower.find(term_lower)
        if index == -1:
            return None
            
        # Get context around the match
        start = max(0, index - context_chars)
        end = min(len(text), index + len(term) + context_chars)
        
        # Adjust to complete words
        while start > 0 and text[start].isalnum():
            start -= 1
        while end < len(text) and text[end-1].isalnum():
            end += 1
            
        return {
            'context': text[start:end],
            'match_start': index - start,
            'match_end': index - start + len(term)
        }

    def perform_search(self):
        query = self.search_var.get().strip()
        if not query:
            self.results_text.delete('1.0', tk.END)
            self.results_text.insert(tk.END, "Please enter a search term.", "header")
            return
        
        self.current_results = self.search_engine.search(query)
        self.current_result_index = 0
        
        self.results_text.delete('1.0', tk.END)
        
        if not self.current_results:
            self.results_text.insert(tk.END, "No matches found.", "header")
            self.update_navigation_buttons()
            return
        
        self.results_text.insert(tk.END, f"Found {len(self.current_results)} matches:\n\n", "header")
        
        # Display first result
        self.display_current_result()
        
        # Update navigation buttons
        self.update_navigation_buttons()

    def display_current_result(self):
        """Display the current search result."""
        if not self.current_results:
            return
        
        # Clear previous results
        self.results_text.delete('1.0', tk.END)
        
        # Get current result
        doc_id, text, score, matches_info = self.current_results[self.current_result_index]
        
        # Insert score with special formatting
        self.results_text.insert(tk.END, "Relevance Score: ", "header")
        self.results_text.insert(tk.END, f"{score:.2f}\n", "score")
        
        # Insert matched terms
        self.results_text.insert(tk.END, "Matched Terms:\n", "header")
        for query_term, matched_term, term_score in matches_info:
            self.results_text.insert(tk.END, 
                f"  '{query_term}' ≈ '{matched_term}' (similarity: {term_score:.2f})\n")
        
        # Show matches in context
        self.results_text.insert(tk.END, "\nMatches in Context:\n", "header")
        for query_term, matched_term, _ in matches_info:
            match_info = self.find_match_in_context(text, matched_term)
            if match_info:
                context = match_info['context']
                start = match_info['match_start']
                end = match_info['match_end']
                
                # Insert context with highlighted match
                self.results_text.insert(tk.END, "  ...")
                self.results_text.insert(tk.END, context[:start])
                self.results_text.insert(tk.END, context[start:end], "match")
                self.results_text.insert(tk.END, context[end:])
                self.results_text.insert(tk.END, "...\n")
        
        # Update result label
        self.result_label.config(text=f"Result {self.current_result_index + 1} of {len(self.current_results)}")

    def show_previous_result(self):
        """Navigate to the previous search result."""
        if self.current_result_index > 0:
            self.current_result_index -= 1
            self.display_current_result()
            self.update_navigation_buttons()

    def show_next_result(self):
        """Navigate to the next search result."""
        if self.current_result_index < len(self.current_results) - 1:
            self.current_result_index += 1
            self.display_current_result()
            self.update_navigation_buttons()

    def update_navigation_buttons(self):
        """Update the state of navigation buttons based on current results."""
        # Update previous button
        if self.current_result_index > 0:
            self.prev_button.config(state=tk.NORMAL)
        else:
            self.prev_button.config(state=tk.DISABLED)
        
        # Update next button
        if self.current_results and self.current_result_index < len(self.current_results) - 1:
            self.next_button.config(state=tk.NORMAL)
        else:
            self.next_button.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = SearchEngineGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()