#Use fiind and string slicing to extract the portion of string after the colon character 
#and use float function to convert extracted string into a floating number

str = 'X-DSPAM-Confidence: 0.8475 '
numpos = str.find(':')
numstr = str[numpos+1:]
numstr = numstr.strip()
num=float(numstr)
print(num)
