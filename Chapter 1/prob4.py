import os

# Specify the directory path ('.' refers to the current working directory)
directory_path = "."

try:
    # Get all files and directories in the specified path
    contents = os.listdir(directory_path)
    
    print(f"Contents of '{directory_path}':\n")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")