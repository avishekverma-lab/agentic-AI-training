# Step 1: Read and print file content line by line
with open("/home/avishek/Avishek/Python/test.log", "r") as file:
    print("-----------------------------------------")
    print("First pass through the file:\n")
    for line in file:
        print(line.strip())

    # Step 2: Go back to the top and print again
    file.seek(28)  # Moves the cursor back to the beginning of the file
    print("-----------------------------------------")
    print("\nSecond pass through the file:\n")
    for line in file:
        print(line.strip())