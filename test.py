import json
import os
# write code to check number of empyt jsonl files in the directory print the file names

import os

def count_empty_jsonl_files(directory):
    empty_jsonl_count = 0

    for filename in os.listdir(directory):
        if filename.endswith('.jsonl'):
            file_path = os.path.join(directory, filename)
            try:
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                    # Check if all lines are empty or contain only whitespace
                    if not lines or all(not line.strip() for line in lines):
                        empty_jsonl_count += 1
                        print(f"Empty JSONL file: {filename}")
            except Exception as e:
                print(f"Error reading {filename}: {e}")
    
    return empty_jsonl_count

# Directory containing `.jsonl` files
directory = 'guj'

# Count and print the number of empty `.jsonl` files
empty_jsonl_count = count_empty_jsonl_files(directory)
print(f"Number of empty JSONL files: {empty_jsonl_count}")
