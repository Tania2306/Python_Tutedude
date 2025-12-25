filename = "output.txt"
inp1 = input("Enter text to write to the file: ")
with open(filename, "w") as file:
    file.write(inp1 + "\n")
print(f"Data successfully written to {filename}.\n")
inp2 = input("Enter additional text to append: ")
with open(filename, "a") as file:
    file.write(inp2 + "\n")
print("Data successfully appended.\n")
print(f"Final content of {filename}:")
with open(filename, "r") as file:
    print(file.read())