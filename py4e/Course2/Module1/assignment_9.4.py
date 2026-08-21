#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

from pathlib import Path

#fname = input("Enter file:")
fname = "mbox-short-copy.txt"

projectpath = str(Path(__file__).resolve().parent.parent.parent)
filepath = projectpath + "/data/" + fname

fh = open(filepath,'r')
emaillist = dict()
prolificcommiter = None
prolificcount = 0
prolificlist = dict()
for line in fh:

    if line.startswith("From "):
        words = line.split()
        emaillist[words[1]]=emaillist.get(words[1],0)+1

for emailid, noofemails in emaillist.items():
    #print(f"{prolificcommiter} sent emails {prolificcount} times" )
    if noofemails > prolificcount:
         prolificcommiter = emailid
         prolificcount = noofemails
prolificlist[prolificcommiter]=prolificlist.get(prolificcommiter, prolificcount)         
for emailid, noofemails in emaillist.items():
    if noofemails == prolificcount:
        prolificlist[emailid]=prolificlist.get(emailid, noofemails)

for emailid, noofemails in prolificlist.items():
    print(f"{emailid} {noofemails}")
        