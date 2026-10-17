# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values 
# and produce an output as shown below. 
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.


# READ: Use the file name mbox-short.txt as the file name
from pathlib import Path

fname = input("Enter the file Name: ")
projectpath = str(Path(__file__).resolve().parent.parent.parent)
fpath = projectpath + "/data/" + fname
try:
    fh = open(fpath)
except:
    print("Entered file could not be found: ", fname)
    quit()
numarray = []
for line in fh:
    if ("X-DSPAM-Confidence:") in line:
        pos = line.find(":")
        numstr = line[pos+1:]
        numstr = numstr.strip()
        num = float(numstr)
        numarray.append(num)

total = 0
for num1 in numarray:
    total = total + num1 

print("Average spam confidence:", total/len(numarray))
