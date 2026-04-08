# File Scanner by Keyword

A simple Python-based tool that scans directories recursively and detects sensitive information based on user-provided keywords.

---

## Features

* Recursively scans folders and subfolders
* Supports `.txt` and `.log` files
* Accepts dynamic keywords via command line
* Ignores encoding errors for better stability
* Displays matched lines with file paths

---

## Usage

```bash
python FileScanner.py <folder_path> <keyword1> <keyword2> ...
```

### Example

```bash
python FileScanner.py . password admin key
```

---

## How It Works

* Takes a folder path and keywords as input
* Traverses all subdirectories using `os.walk()`
* Opens each `.txt` and `.log` file
* Searches for keyword matches (case-insensitive)
* Prints matching lines with file location

---

## Requirements

* Python 3.x

---

## Notes

* Ensure correct folder path is provided
* Use lowercase keywords for consistent matching
* Some restricted files may not be accessible

---

## Future Improvements

* Add regex-based searching
* Export results to a file
* Add file type filters
* Improve CLI using `argparse`

---

## Author

Sameer Kumar

---
