# Python Scan Files & Folders

## installation

Use the package manager [pip] (https://pip.pypa.io/en/stable/) to install os

```bash 
pip install os
```

## Usage

```python
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
```

## Output

![alt text](https://github.com/[sourovpal]/[python-scan-all-file-and-folder]/blob/[master]/screenshot_1.png?raw=true)