from pathlib import Path
import re

try:
    filepath = str(Path(__file__).resolve().parent.parent) + "/data/" + "regex_sum_2267528.txt"
    fh = open(filepath, 'r')
except:
    print("Error opening file: ", filepath)
    quit

txt = fh.read()
lst = re.findall('[0-9]+' , txt)
print(lst)
print('***************************************')
for i in range(len(lst)):
    lst[i] = int(lst[i])

print(sum(lst))

#print(re.findall('[0-9]+', fh.read()))


