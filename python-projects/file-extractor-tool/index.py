import os
import zipfile
import tarfile

def _is_within_directory(directory, target):
    directory = os.path.abspath(directory)
    target = os.path.abspath(target)
    return os.path.commonpath([directory]) == os.path.commonpath([directory, target])

class FileExtractor:
    def __init__(self, source_path, dest_path):
        self.source_path = source_path
        self.dest_path = dest_path
        if not os.path.exists(self.dest_path):
            os.makedirs(self.dest_path)

    def extract_zip(self):
        if zipfile.is_zipfile(self.source_path):
            with zipfile.ZipFile(self.source_path, 'r') as zip_ref:
                for member in zip_ref.namelist():
                    member_path = os.path.join(self.dest_path, member)
                    if not _is_within_directory(self.dest_path, member_path):
                        return "Blocked unsafe ZIP entry (path traversal attempt)."
                zip_ref.extractall(self.dest_path)
            return "ZIP file extracted successfully."
        else:
            return "Not a valid ZIP file."

    def extract_tar(self):
        if tarfile.is_tarfile(self.source_path):
            with tarfile.open(self.source_path, 'r:*') as tar_ref:
                for member in tar_ref.getmembers():
                    member_path = os.path.join(self.dest_path, member.name)
                    if not _is_within_directory(self.dest_path, member_path):
                        return "Blocked unsafe TAR entry (path traversal attempt)."
                tar_ref.extractall(self.dest_path)
            return "TAR file extracted successfully."
        else:
            return "Not a valid TAR file."

    def extract_file(self):
        print(f"Source path: {self.source_path}")
        print(f"Destination path: {self.dest_path}")
        
        if not os.path.exists(self.source_path):
            return "File does not exist."
        
        if self.source_path.lower().endswith('.zip'):
            print("Detected ZIP file.")
            return self.extract_zip()
        elif self.source_path.lower().endswith(('.tar', '.tar.gz', '.tgz', '.tar.bz2')):
            print("Detected TAR file.")
            return self.extract_tar()
        else:
            return "Unsupported file format."

# Example usage:
if __name__ == "__main__":
    source = input("Enter the path of the file to extract: ")
    destination = input("Enter the destination folder: ")

    extractor = FileExtractor(source, destination)
    result = extractor.extract_file()
    print(result)