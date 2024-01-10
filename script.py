import os
import sys
import random

NUMBER_OF_FILES = 60

def select_and_delete(folder_path):
    try:
        # Get a list of all subfolders in the given folder
        subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]

        # Process each subfolder
        for subfolder in subfolders:
            print(f"Processing folder: {subfolder}")

            # Get a list of all files in the subfolder
            files = [f.path for f in os.scandir(subfolder) if f.is_file()]

            # Randomly select 'NUMBER_OF_FILES' files
            selected_errors = random.sample(files, min(NUMBER_OF_FILES, len(files)))

            # Delete the non-selected files
            for file in files:
                if file not in selected_errors:
                    os.remove(file)
                    print(f"Deleted: {file}")

    except FileNotFoundError:
        print(f"Error: The folder '{folder_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if a folder path is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <main_folder_path>")
    else:
        main_folder_path = sys.argv[1]
        select_and_delete(main_folder_path)
