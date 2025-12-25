import os

# Define the filename
filename = "sample.txt"

# Check if the file exists in the current directory
if os.path.exists(filename):
    # Open and read the file
    with open(filename, "r") as file:
        print("Reading file content:")
        
        # Print content line by line with numbering
        for index, line in enumerate(file, start=1):
            # .strip() removes trailing newlines for clean output
            print(f"Line {index}: {line.strip()}")
else:
    # Graceful error handling if file is missing
    print(f"Error: The file '{filename}' was not found.")