import os
import shutil
import argparse

def revert_organize_files(directory, mapping_file):
    with open(mapping_file, 'r') as file:
        mapping = eval(file.read())

    for new_path, original_path in mapping.items():
        source_path = os.path.join(directory, new_path)
        target_path = os.path.join(directory, original_path)

        if not os.path.exists(os.path.dirname(target_path)):
            os.makedirs(os.path.dirname(target_path))

        shutil.move(source_path, target_path)

    # Remove empty directories created during organization
    for root, dirs, _ in os.walk(directory, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            try:
                os.rmdir(dir_path)
            except OSError:
                pass

def main():
    parser = argparse.ArgumentParser(description="Manually revert back to the original file structure in a directory.")
    parser.add_argument("directory", help="The directory path to revert.")
    args = parser.parse_args()

    if not os.path.exists(args.directory):
        print(f"Error: Directory '{args.directory}' not found.")
        return

    revert_organize_files(args.directory, "./mapping.json")
    print(f"Files in '{args.directory}' reverted successfully.")

if __name__ == "__main__":
    main()
