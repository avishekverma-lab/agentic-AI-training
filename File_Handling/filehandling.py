file = open("/home/avishek/Avishek/Python/test.log", "r")

# Read contents
content = file.read()
print(content)

file.close()

file = open("/home/avishek/Avishek/Python/test.log", "a")
file.write("\nHello, this is a 3nd line.\n")

content = file.read()
print(content)

# Always close the file

file.close()