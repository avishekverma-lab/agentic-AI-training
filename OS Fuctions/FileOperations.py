import os

# Step 1: Create a new directory
dir_name = "my_directory"
os.makedirs(dir_name, exist_ok=True)  # exist_ok=True avoids error if it already exists
print(f"Directory '{dir_name}' created.")

# Step 2: Create and open a text file in that directory
file_path = os.path.join(dir_name, "myfile.txt")
print("File path:", file_path)

# Step 3: Write a line into the file
with open(file_path, "w") as f:
    f.write("this is second line in this file\n")
    print("Line written and file closed.")

# Step 4: Open the file again and print its content
with open(file_path, "r") as f:
    content = f.read()
    print("File content:")
    print(content)

# File is automatically closed after 'with' block
