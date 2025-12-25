import os
filepath = r"C:\Users\TANIA ROBBY\Desktop\Python_Tutedude\sample.txt"
if os.path.exists(filepath):
    with open(filepath, "r") as file:
        print("Reading file content:")
        
        for index, line in enumerate(file, start=1):
            print(f"Line {index}: {line.strip()}")
else:
    filename = os.path.basename(filepath)
    print(f"Error: The file '{filename}' was not found at {filepath}")