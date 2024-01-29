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

# Find duplicate and unique files between source and target
def find_duplicates_uniques(source_dir, target_dir):
    source_files = get_files_with_hashes(source_dir)
    target_files = get_files_with_hashes(target_dir)

    # list comprehensions comparing source files to target, find matches, find unqiues
    matches = [file for file, hash in source_files.items() if hash in target_files.values()]
    uniques = [file for file, hash in source_files.items() if hash not in target_files.values()]

    return matches, uniques # return the lists

# Write resulting paths to specified file
def write_to_file(file_list, file_name):
    with open(file_name, 'w') as file:
        for item in file_list:
            file.write(f"{item}\n")

# Main function to invoke operation
def main(source_dir, target_dir):
    if not os.path.isdir(source_dir) or not os.path.isdir(target_dir): # check if paths are directories
        print('One or both of the provided paths are not directories')
        sys.exit(1)

    # Find duplicates and uniques and write them to respective output files
    matches, uniques = find_duplicates_uniques(source_dir, target_dir)
    write_to_file(matches, 'matches.txt')
    write_to_file(uniques, 'uniques.txt')
    print("Process complete. Check 'matches.txt' and 'uniques.txt' for results")
        