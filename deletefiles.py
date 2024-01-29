import os
import sys

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"Deleted: {file_path}")
    except OSError as e:
        print(f"Error: {e.strerror}. File: {file_path}")
        