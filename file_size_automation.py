import os
import shutil

def get_size_category(size):
    """Categorize files based on size in bytes."""
    if size < 1_000_000:  # Less than 1MB
        return 'Small'
    elif 1_000_000 <= size < 10_000_000:  # Between 1MB and 10MB
        return 'Medium'
    else:  # Larger than 10MB
        return 'Large'

def organize_by_size(directory):
    # List all files in the directory
    for filename in os.listdir(directory):
        # Construct full file path
        file_path = os.path.join(directory, filename)

        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue
        
        # Get the file size in bytes
        size = os.path.getsize(file_path)
        size_category = get_size_category(size)

        # Create a folder for the size category if it doesn't exist
        folder_path = os.path.join(directory, size_category)
        os.makedirs(folder_path, exist_ok=True)
        
        # Move the file to the corresponding folder
        shutil.move(file_path, os.path.join(folder_path, filename))

    print("Files organized by size.")

# Use the function
organize_by_size(r'C:\Users\shiva\Pictures\New folder\Data')  # Replace with your directory path

#python file_size_automation.py