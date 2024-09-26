import os
import shutil

# Define the directory to organize
DIRECTORY_TO_ORGANIZE = 'D:\Python\Others'  # Replace with your directory path

# Define file type categories and their extensions
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx', '.xls', '.xlsx'],
    'Audio': ['.mp3', '.wav', '.aac', '.ogg'],
    'Video': ['.mp4', '.mkv', '.mov', '.avi'],
    'Archives': ['.zip', '.tar', '.gz', '.rar'],
    'Others': []
}

def organize_files(directory):
    # Create category directories if they do not exist
    for category in FILE_CATEGORIES.keys():
        category_path = os.path.join(directory, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
    
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue
        
        # Get the file extension
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()

        # Determine the category based on the extension
        moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                # Move the file to the corresponding category folder
                shutil.move(file_path, os.path.join(directory, category, filename))
                moved = True
                print(f'Moved: {filename} to {category}/')
                break
        
        if not moved:
            # Move to 'Others' if no category matches
            shutil.move(file_path, os.path.join(directory, 'Others', filename))
            print(f'Moved: {filename} to Others/')

if __name__ == "__main__":
    organize_files(DIRECTORY_TO_ORGANIZE)