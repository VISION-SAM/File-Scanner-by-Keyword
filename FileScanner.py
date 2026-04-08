## This tool scans folders and finds sensitive data as per provided keyword.
# this program is updated version of FileScanner.py, This takes location from the user input
# Usage: python FileScanner.py <folder_path> <keyword1> <keyword2> ...

import os
import sys

if len(sys.argv) < 3:
    print("Usage: python FileScanner.py <folder_path> <keyword1> <keyword2> ...")
    sys.exit(1)

folder_path = sys.argv[1]

keywords = [word.lower() for word in sys.argv[2:]]

count = 0

for root, dirs, files in os.walk(folder_path):
    for file in files:
            if file.endswith(".txt") or file.endswith(".log"):
                
                full_path = os.path.join(root, file)

                try:
                    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                        for line in f:
                            if any(word in line.lower() for word in keywords):
                                print(f"[!] {full_path}: {line.strip()}")
                                count += 1
                                
                except Exception as e:
                    print(f"Error Reading {full_path}: {e}")
print(f"Total Maches : ", count)
                    
