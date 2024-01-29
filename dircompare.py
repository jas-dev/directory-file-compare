import os
import hashlib
import sys

# Calculate the md5 hash of a file
def get_file_hash(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        buf = file.read()
        hasher.update(buf)
    return hasher.hexdigest()

# Get a dictionary map of file paths to their md5 hash value
def get_files_with_hashes(directory):
    files_hash_map = {}
    for root, dirs, files in os.walk(directory): # traverse directory tree. dirs unpacked but wont be used for now
        for file in files:
            file_path = os.path.join(root,file) # get full file path
            file_hash = get_file_hash(file_path) # compute hash of file
            files_hash_map[file_path] = file_hash # map file path to its hash
    return files_hash_map
