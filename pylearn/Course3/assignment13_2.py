import urllib.request, urllib.parse, urllib.error
import ssl
import json

url = input("Enter URL here: ")
print("retriving details from ", url,"...")

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

json_data = urllib.request.urlopen(url, context=ctx).read()
content = json.loads(json_data)
text = str(content)

comments_list = content['comments']
commnent_total = 0

for comment in comments_list:
    commnent_total = commnent_total+ int((comment['count']))

print("Retreived ", len(text), " characters")
print("Count of comments = ", len(comments_list))
print("Sum of comments = ", commnent_total)
