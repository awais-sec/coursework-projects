import hashlib
import os
import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import Calendar, DateEntry
from datetime import datetime

# Password hashing helpers
def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(16).hex()
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), bytes.fromhex(salt), 100_000).hex()
    return f"{salt}${digest}"

def verify_password(password, stored):
    salt, _ = stored.split("$", 1)
    return hash_password(password, salt) == stored

# Initialize database connection
def init_db():
    conn = sqlite3.connect("event_planner.db")
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Bookings (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        customer_name TEXT NOT NULL,
                        event_date TEXT NOT NULL,
                        event_type TEXT,
                        services TEXT,
                        menu TEXT,
                        num_people INTEGER,
                        estimated_cost REAL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Notes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        note_date TEXT NOT NULL,
                        note TEXT NOT NULL)''')

    conn.commit()
    conn.close()

# Register User
def register_user(username, password):
    conn = sqlite3.connect("event_planner.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)", (username, hash_password(password)))
        conn.commit()
        messagebox.showinfo("Success", "Registration successful!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists!")
    finally:
        conn.close()

# Authenticate User
def login_user(username, password):
    conn = sqlite3.connect("event_planner.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM Users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()
    if row and verify_password(password, row[0]):
        return True
    return False

# Add Booking
def add_booking(customer_name, event_date, event_type, services, menu, num_people, estimated_cost):
    conn = sqlite3.connect("event_planner.db")
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Bookings (customer_name, event_date, event_type, services, menu, num_people, estimated_cost)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''', (customer_name, event_date, event_type, services, menu, num_people, estimated_cost))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Booking added successfully!")

# View Bookings
def view_bookings():
    conn = sqlite3.connect("event_planner.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Bookings")
    bookings = cursor.fetchall()
    conn.close()
    return bookings

# Delete Booking
def delete_booking(booking_id):
    conn = sqlite3.connect("event_planner.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Bookings WHERE id = ?", (booking_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Booking deleted successfully!")

# Add Note
def add_note(note_date, note):
    conn = sqlite3.connect("event_planner.db")
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Notes (note_date, note) VALUES (?, ?)''', (note_date, note))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Note added successfully!")

# View Notes
def view_notes():
    conn = sqlite3.connect("event_planner.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Notes")
    notes = cursor.fetchall()
    conn.close()
    return notes

# Count Monthly Bookings
def count_monthly_bookings():
    conn = sqlite3.connect("event_planner.db")
    cursor = conn.cursor()
    current_month = datetime.now().strftime("%Y-%m")
    cursor.execute("SELECT COUNT(*) FROM Bookings WHERE event_date LIKE ?", (f"{current_month}%",))
    count = cursor.fetchone()[0]
    conn.close()
    return count

# GUI Initialization
def init_gui():
    root = Tk()
    root.title("Event Planner Pro")
    root.geometry("1024x768")
    root.configure(bg="#ffffff")

    style = ttk.Style()
    style.configure("TButton", font=("Arial", 12), padding=5)
    style.configure("TLabel", font=("Arial", 12), background="#ffffff")
    style.configure("TEntry", font=("Arial", 12))

    current_user = [None]  # Track the currently logged-in user

    def switch_to_dashboard():
        for widget in root.winfo_children():
            widget.destroy()
        show_dashboard()

    def show_register():
        for widget in root.winfo_children():
            widget.destroy()

        ttk.Label(root, text="Register", font=("Arial", 20)).pack(pady=20)

        ttk.Label(root, text="Username:").pack(pady=5)
        username_entry = ttk.Entry(root)
        username_entry.pack(pady=5)

        ttk.Label(root, text="Password:").pack(pady=5)
        password_entry = ttk.Entry(root, show="*")
        password_entry.pack(pady=5)

        ttk.Button(root, text="Register", command=lambda: register_user(username_entry.get(), password_entry.get())).pack(pady=10)
        ttk.Button(root, text="Back to Login", command=show_login).pack(pady=10)

    def show_login():
        for widget in root.winfo_children():
            widget.destroy()

        ttk.Label(root, text="Login", font=("Arial", 20)).pack(pady=20)

        ttk.Label(root, text="Username:").pack(pady=5)
        username_entry = ttk.Entry(root)
        username_entry.pack(pady=5)

        ttk.Label(root, text="Password:").pack(pady=5)
        password_entry = ttk.Entry(root, show="*")
        password_entry.pack(pady=5)

        def attempt_login():
            if login_user(username_entry.get(), password_entry.get()):
                current_user[0] = username_entry.get()
                switch_to_dashboard()
            else:
                messagebox.showerror("Error", "Invalid credentials!")

        ttk.Button(root, text="Login", command=attempt_login).pack(pady=10)
        ttk.Button(root, text="Register", command=show_register).pack(pady=10)

    def show_dashboard():
        ttk.Label(root, text=f"Welcome, {current_user[0]}", font=("Arial", 16)).pack(pady=10)

        menu_frame = Frame(root, bg="#ffffff")
        menu_frame.pack(side=LEFT, fill=Y, padx=10)

        ttk.Button(menu_frame, text="Add Booking", width=20, command=show_booking_form).pack(pady=10)
        ttk.Button(menu_frame, text="View Bookings", width=20, command=show_view_bookings).pack(pady=10)
        ttk.Button(menu_frame, text="Calendar View", width=20, command=show_calendar_view).pack(pady=10)
        ttk.Button(menu_frame, text="Statistics", width=20, command=show_statistics).pack(pady=10)
        ttk.Button(menu_frame, text="About", width=20, command=show_about).pack(pady=10)
        ttk.Button(menu_frame, text="Logout", width=20, command=show_login).pack(pady=10)

        main_frame = Frame(root, bg="#f8f9fa")
        main_frame.pack(side=RIGHT, expand=True, fill=BOTH)

        ttk.Label(main_frame, text="Dashboard", font=("Arial", 20), background="#f8f9fa").pack(pady=20)

    def clear_and(build_fn):
        for widget in root.winfo_children():
            widget.destroy()
        build_fn()

    def show_booking_form():
        for widget in root.winfo_children():
            widget.destroy()

        ttk.Label(root, text="Add Booking", font=("Arial", 20)).pack(pady=15)

        form = Frame(root, bg="#ffffff")
        form.pack(pady=10)

        ttk.Label(form, text="Customer Name:").grid(row=0, column=0, sticky=E, padx=5, pady=5)
        customer_entry = ttk.Entry(form)
        customer_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form, text="Event Date:").grid(row=1, column=0, sticky=E, padx=5, pady=5)
        date_entry = DateEntry(form, date_pattern="yyyy-mm-dd")
        date_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(form, text="Event Type:").grid(row=2, column=0, sticky=E, padx=5, pady=5)
        event_type_entry = ttk.Entry(form)
        event_type_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(form, text="Services:").grid(row=3, column=0, sticky=E, padx=5, pady=5)
        services_entry = ttk.Entry(form)
        services_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(form, text="Menu:").grid(row=4, column=0, sticky=E, padx=5, pady=5)
        menu_entry = ttk.Entry(form)
        menu_entry.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(form, text="Number of People:").grid(row=5, column=0, sticky=E, padx=5, pady=5)
        num_people_entry = ttk.Entry(form)
        num_people_entry.grid(row=5, column=1, padx=5, pady=5)

        ttk.Label(form, text="Estimated Cost:").grid(row=6, column=0, sticky=E, padx=5, pady=5)
        cost_entry = ttk.Entry(form)
        cost_entry.grid(row=6, column=1, padx=5, pady=5)

        def submit_booking():
            customer_name = customer_entry.get().strip()
            event_date = date_entry.get_date().strftime("%Y-%m-%d")
            event_type = event_type_entry.get().strip()
            services = services_entry.get().strip()
            menu = menu_entry.get().strip()

            if not customer_name:
                messagebox.showerror("Error", "Customer name is required.")
                return

            try:
                num_people = int(num_people_entry.get()) if num_people_entry.get().strip() else 0
            except ValueError:
                messagebox.showerror("Error", "Number of people must be a whole number.")
                return

            try:
                estimated_cost = float(cost_entry.get()) if cost_entry.get().strip() else 0.0
            except ValueError:
                messagebox.showerror("Error", "Estimated cost must be a number.")
                return

            add_booking(customer_name, event_date, event_type, services, menu, num_people, estimated_cost)
            switch_to_dashboard()

        ttk.Button(root, text="Save Booking", command=submit_booking).pack(pady=10)
        ttk.Button(root, text="Back to Dashboard", command=switch_to_dashboard).pack(pady=5)

    def show_view_bookings():
        for widget in root.winfo_children():
            widget.destroy()

        ttk.Label(root, text="Bookings", font=("Arial", 20)).pack(pady=15)

        columns = ("id", "customer_name", "event_date", "event_type", "services", "menu", "num_people", "estimated_cost")
        tree = ttk.Treeview(root, columns=columns, show="headings", height=15)
        for col in columns:
            tree.heading(col, text=col.replace("_", " ").title())
            tree.column(col, width=110)
        tree.pack(pady=10, padx=10, fill=BOTH, expand=True)

        for booking in view_bookings():
            tree.insert("", END, values=booking)

        def delete_selected():
            selected = tree.selection()
            if not selected:
                messagebox.showerror("Error", "Select a booking to delete.")
                return
            booking_id = tree.item(selected[0])["values"][0]
            delete_booking(booking_id)
            clear_and(show_view_bookings)

        button_frame = Frame(root, bg="#ffffff")
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Delete Selected", command=delete_selected).pack(side=LEFT, padx=5)
        ttk.Button(button_frame, text="Back to Dashboard", command=switch_to_dashboard).pack(side=LEFT, padx=5)

    def show_calendar_view():
        for widget in root.winfo_children():
            widget.destroy()

        ttk.Label(root, text="Calendar View", font=("Arial", 20)).pack(pady=15)

        cal = Calendar(root, selectmode="day", date_pattern="yyyy-mm-dd")
        cal.pack(pady=10)

        bookings_by_date = {}
        for booking in view_bookings():
            bookings_by_date.setdefault(booking[2], []).append(booking)
            cal.calevent_create(datetime.strptime(booking[2], "%Y-%m-%d"), booking[1], "booking")
        cal.tag_config("booking", background="#ffd966")

        details_label = ttk.Label(root, text="Select a date to see bookings.", justify=LEFT)
        details_label.pack(pady=10)

        def on_date_selected(event):
            selected_date = cal.get_date()
            day_bookings = bookings_by_date.get(selected_date, [])
            if day_bookings:
                lines = [f"- {b[1]} ({b[3]})" for b in day_bookings]
                details_label.config(text=f"Bookings on {selected_date}:\n" + "\n".join(lines))
            else:
                details_label.config(text=f"No bookings on {selected_date}.")

        cal.bind("<<CalendarSelected>>", on_date_selected)

        ttk.Button(root, text="Back to Dashboard", command=switch_to_dashboard).pack(pady=10)

    def show_statistics():
        for widget in root.winfo_children():
            widget.destroy()

        ttk.Label(root, text="Statistics", font=("Arial", 20)).pack(pady=15)

        all_bookings = view_bookings()
        total_bookings = len(all_bookings)
        monthly_bookings = count_monthly_bookings()
        total_revenue = sum(b[7] for b in all_bookings)

        stats_frame = Frame(root, bg="#ffffff")
        stats_frame.pack(pady=20)

        ttk.Label(stats_frame, text=f"Total Bookings: {total_bookings}", font=("Arial", 14)).pack(pady=5)
        ttk.Label(stats_frame, text=f"Bookings This Month: {monthly_bookings}", font=("Arial", 14)).pack(pady=5)
        ttk.Label(stats_frame, text=f"Total Estimated Revenue: {total_revenue:,.2f}", font=("Arial", 14)).pack(pady=5)

        ttk.Button(root, text="Back to Dashboard", command=switch_to_dashboard).pack(pady=10)

    def show_about():
        for widget in root.winfo_children():
            widget.destroy()

        ttk.Label(root, text="About Event Planner Pro", font=("Arial", 20)).pack(pady=15)
        ttk.Label(
            root,
            text="Event Planner Pro helps you manage event bookings,\n"
                 "track a calendar of upcoming events, and review\n"
                 "booking statistics — all backed by a local SQLite database.",
            justify=CENTER,
        ).pack(pady=10)

        ttk.Button(root, text="Back to Dashboard", command=switch_to_dashboard).pack(pady=10)

    show_login()
    root.mainloop()

# Initialize database
init_db()

# Start the GUI
init_gui()
