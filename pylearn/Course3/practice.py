from pathlib import Path
import re

projectpath =str(Path(__file__).resolve().parent.parent)

filename = "mbox-short-copy.txt"
filepath = projectpath + '/data/' + filename


text = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
amt = re.findall(r'\S+@\S+', text)
print(amt)

# fh = open(filepath, 'r')
# numlist = list()
# for line in fh:
#     line = line.rstrip()
    # dspam = re.findall('^X-DSPAM-Confidence: ([0-9].+)', line)
    # if len(dspam) != 1 : continue
    # dspamnum = float(dspam[0])
    # numlist.append(dspamnum)
    # email = re.findall('^From: ([a-z]+.*)', line)
    # if len(email) != 1 : continue
    # domain = re.findall('@(\S+)',email[0])
    # print(domain)
        
#print(max(numlist))

#fh.close