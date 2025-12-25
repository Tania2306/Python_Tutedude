**Assignment 4 - Task 1**
This program access a file and reads the content in it line by line.
import os => built-in module : allows python to access the computer's files.
filename => variable to store the name of the file.
if => runs the block of code under it if the condition specified is true.
else => runs the block of code under it if the condition specified is not true.
os.path.exists() => function from os module : checks if the specified file exists in the system.
with => ensures that the file is closed automatically once the task is done
open() => used to open the the file in python
r => specifies Read Mode (only reads the data, does not not delete or edit it).
enumerate => built in function to keep track of the count in for loop. In this file it keeps tracl of the lines in the file.
.strip() => removes whitespaces and hidden new line characters.


**Assignment 4 - Task 2**
This program creates a files, takes input from the user and writes in that file. It also appends additional data in the file.
filename => stores the name of the file : "output.txt".
inp1 => user input for the data to be written in the file.
with => ensures that the file is closed automatically once the task is done.
open => used to open the the file in python.
w => opens file in write mode.
.write() => used to write in the file.
file.write(inp1 + "\n") => used to write the inp1 in the file and start a new line with additional data.
inp2 => user input for the additional data to be appended in the file.
a => when used with open(), it opens the file in Append mode.
open(filename, "r") => opens the file in read mode.
print(file.read()) => prints the data in the file.

