# File Organizer

## Overview

The File Organizer is a Python script designed to organize files within a specified directory based on their file types. It helps maintain a structured and organized file system by categorizing files into folders according to their extensions.

## Features

- **Organize Files Script:** The `organize_files.py` script scans the specified directory, categorizes files based on their extensions, and moves them into corresponding folders. It also generates a mapping file (`mapping.json`) to track the changes.

- **Revert Organization Script:** The `revert_organize_files.py` script uses the mapping file to revert the changes made by the organization script, restoring the original file structure.

## How to Use

1. **Installation:**

   - Clone the repository:

     ```bash
     git clone https://github.com/kunal232i/File-Organizer.git
     ```

   - Navigate to the project directory:

     ```bash
     cd File-Organizer
     ```

2. **Organize Files:**

   ```bash
   python organize_files.py <directory_path>
   ```

   - Replace `<directory_path>` with the path of the directory you want to organize.

3. **Revert Organization:**

   ```bash
   python revert_organize_files.py <directory_path>
   ```

   - Replace `<directory_path>` with the path of the directory you want to revert.

## Example

Organizing files in the `example_directory`:

```bash
python organize_files.py example_directory
```

Reverting the organization in the `example_directory`:

```bash
python revert_organize_files.py example_directory
```

## Note

- The mapping of the file structure is stored in `mapping.json`.
- If files are accidentally organized, the revert script can be used to restore the original structure.

## GIF

![organize_files_gif](https://github.com/kunal232i/File-Organizer/assets/81668653/56598bb6-63cf-4bec-a256-367db2c56132)

