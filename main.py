import os

# Folder path 
path = "./"

# Scan all file & folder
dir_list = os.listdir(path)

# Find all Folders
folders = [d for d in dir_list if os.path.isdir(d)]

# Find All Files
files = [d for d in dir_list if os.path.isfile(d)]

# Print Folders
print(folders)

# Print Files
print(files)