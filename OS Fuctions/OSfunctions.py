import os
print ("#" * 60)
# Get current working directory
print("Current directory:", os.getcwd())

# List files in current directory
print("Files:", os.listdir())

# Create a new folder
os.mkdir("new_folder")

# Remove a folder
os.rmdir("new_folder")

# Rename a file
#os.rename("old.txt", "new.txt")


# Operating system name
print("OS name:", os.name)

# Environment variables
print("PATH:", os.environ.get("PATH"))

# CPU count
print("CPU cores:", os.cpu_count())

print ("#" * 60)
# Run a shell command
os.system("echo Hello from Python")

# On Windows: open Notepad
#os.system("notepad")

# On Linux/macOS: list files
os.system("dir" if os.name == "nt" else "ls -l")

print ("#" * 60)
import os

path = "/home/user/file.txt"

print("Directory:", os.path.dirname(path))
print("File name:", os.path.basename(path))
print("Exists?", os.path.exists(path))
print("Absolute path:", os.path.abspath("file.txt"))

print ("#" * 60)
################################################################################
# Get current working directory
current_dir = os.getcwd()
print("Current directory:", current_dir)

# Get parent directory
parent_dir = os.path.dirname(current_dir)
print("Parent directory:", parent_dir)

# Change to parent directory
os.chdir(parent_dir)
print("Now in:", os.getcwd())
################################################################################

print ("#" * 60)