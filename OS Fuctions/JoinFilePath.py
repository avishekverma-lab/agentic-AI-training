import os

folder = "new_directory"
filename = "sample.txt"

file_path = os.path.join(folder, filename)

print(file_path)