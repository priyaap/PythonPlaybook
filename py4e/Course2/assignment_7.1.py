#7.1 Write a program that prompts for a file name, then opens that file and 
# reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
#You can download the sample data at http://www.py4e.com/code3/words.txt

# READ: For the assignment sake please Use words.txt as the file name
from pathlib import Path

fname = input("Enter file name: ")
projectpath = str(Path(__file__).resolve().parent.parent.parent)
filepath = projectpath + "/data/" + fname
fh = open(filepath)
for line in fh:
    line = line.strip()
    print(line.upper())
