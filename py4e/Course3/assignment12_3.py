import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#SAMPLE PROBLEM SOLUTION
# url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'

# for j in range(4):
#     html = urllib.request.urlopen(url, context=ctx).read()
#     soup = BeautifulSoup(html, 'html.parser')
#     tags = soup('a')
#     for i in range(len(tags)):
#         if i == 2:
            
#             last_name = tags[i].contents[0]
            
#             url=tags[i].get('href', None)
#             break
    
# print("Answer: ",last_name)

#ACTUAL PROBLEM SOLUTION

url = 'http://py4e-data.dr-chuck.net/known_by_Kati.html'

for j in range(7):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for i in range(len(tags)):
        if i == 17:
            
            last_name = tags[i].contents[0]
            
            url=tags[i].get('href', None)
            break
    
print("Answer: ",last_name)
