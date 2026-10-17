# Handling The Data
# The basic outline of this problem is to read the file, look for integers using the re.findall(), 
# looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.
# Optional: Just for Fun
# There are a number of different ways to approach this problem. 
# While we don't recommend trying to write the most compact code possible, it can sometimes be a fun exercise. 
# # Here is a a redacted version of two-line version of this program using list comprehension:
# Please don't waste a lot of time trying to figure out the shortest solution until you have completed the homework. 
# List comprehension is mentioned in Chapter 10 and the read() method is covered in Chapter 7.

from pathlib import Path
import re

projectpath = str(Path(__file__).resolve().parent.parent)
filename = 'regex_sum_2267528.txt'
filepath = projectpath + '/data/' + filename

fh = open(filepath, 'r')

numlist = list()

for line in fh:
    nums = re.findall('[0-9]+', line)
    if len(nums) == 0: continue
    for num in nums:
        num = int(num)
        numlist.append(num)

fh.close

print(sum(numlist))
