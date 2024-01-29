import os
import sys

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"Deleted: {file_path}")

    except OSError as e:
        print(f"Error: {e.strerror}. File: {file_path}")

def process_file(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:

                # Handle both lineseparated and comma-separated values
                file_paths = line.strip().split(',')
                for path in file_paths:
                    if path: # check path is not empty
                        delete_file(path.strip())

    except FileNotFoundError:
        print(f'File not found: {file_name}')
    except Exception as e:
        print(f'Error: {e}')