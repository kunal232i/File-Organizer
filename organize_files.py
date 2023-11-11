import os
import shutil
import argparse
import json

def organize_files(directory, mapping_file):
    mapping = {}

    for root, _, files in os.walk(directory):
        for filename in files:
            _, extension = os.path.splitext(filename)
            extension = extension[1:].lower()

            source_path = os.path.join(root, filename)
            target_dir = os.path.join(directory, extension)

            target_path = os.path.join(target_dir, filename)
            counter = 1
            while os.path.exists(target_path):
                base, ext = os.path.splitext(filename)
                filename = f"{base}_{counter}{ext}"
                target_path = os.path.join(target_dir, filename)
                counter += 1

            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

            shutil.move(source_path, target_path)

            # Store mapping information
            relative_path = os.path.relpath(target_path, directory)
            mapping[relative_path] = os.path.relpath(source_path, directory)

    # Save mapping to a JSON file
    with open(mapping_file, 'w') as json_file:
        json.dump(mapping, json_file, indent=4)

def main():
    parser = argparse.ArgumentParser(description="Organize files in a directory based on their file type and store the mapping.")
    parser.add_argument("directory", help="The directory path to organize.")
    args = parser.parse_args()

    if not os.path.exists(args.directory):
        print(f"Error: Directory '{args.directory}' not found.")
        return

    organize_files(args.directory, "./mapping.json")
    print(f"Files in '{args.directory}' organized successfully.")

if __name__ == "__main__":
    main()
