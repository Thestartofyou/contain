import os
import shutil

# Define the source directory where the files are located.
source_directory = "C:/YourSourceDirectory"

# Define the target directory where the organized folders will be created.
target_directory = "C:/YourTargetDirectory"

# Create a dictionary to map tags to folder names.
tag_to_folder = {
    "Documents": "Documents",
    "Images": "Images",
    "Videos": "Videos",
    "Music": "Music",
    "Other": "Other"
}

# Create folders for each tag in the target directory.
for folder in tag_to_folder.values():
    os.makedirs(os.path.join(target_directory, folder), exist_ok=True)

# Function to organize files based on tags.
def organize_files(source_dir, target_dir):
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        
        # Check if it's a file (not a subdirectory).
        if os.path.isfile(source_path):
            # Get the file extension.
            file_extension = os.path.splitext(filename)[1].lower()
            
            # Determine the tag based on the file extension.
            if file_extension in (".txt", ".pdf", ".doc", ".docx"):
                tag = "Documents"
            elif file_extension in (".jpg", ".jpeg", ".png", ".gif"):
                tag = "Images"
            elif file_extension in (".mp4", ".avi", ".mov"):
                tag = "Videos"
            elif file_extension in (".mp3", ".wav", ".flac"):
                tag = "Music"
            else:
                tag = "Other"
            
            # Move the file to the corresponding folder.
            target_folder = os.path.join(target_dir, tag_to_folder[tag])
            shutil.move(source_path, os.path.join(target_folder, filename))
            print(f"Moved {filename} to {tag_to_folder[tag]} folder.")

# Organize the files.
organize_files(source_directory, target_directory)
