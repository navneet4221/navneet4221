import os
import shutil

# Define the directory to organize
directory_to_organize = 'path/to/your/directory'

# Define file extensions and corresponding folder names
extension_mapping = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Spreadsheets': ['.xlsx', '.csv'],
    'Presentations': ['.pptx'],
    'Audio': ['.mp3', '.wav'],
    'Video': ['.mp4', '.avi'],
    # Add more categories as needed
}

# Create the folders if they don't exist
for folder_name in extension_mapping.keys():
    folder_path = os.path.join(directory_to_organize, folder_name)
    os.makedirs(folder_path, exist_ok=True)

# Move files to the corresponding folders
for filename in os.listdir(directory_to_organize):
    file_path = os.path.join(directory_to_organize, filename)
    if os.path.isfile(file_path):
        for folder_name, extensions in extension_mapping.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                # Move the file to the corresponding folder
                shutil.move(file_path, os.path.join(directory_to_organize, folder_name, filename))
                print(f'Moved: {filename} to {folder_name}')
                break

print("Organization complete!")
