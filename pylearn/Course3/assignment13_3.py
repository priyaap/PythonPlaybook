import urllib.request, urllib.parse, urllib.error
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input("Enter location: ")

#address = '24 E Washington St. Chicago, IL 60602'
address = address.strip()

endpoint = 'https://py4e-data.dr-chuck.net/opengeo?'
param = dict()
param['q'] = address

url = endpoint + urllib.parse.urlencode(param)
print("Retrieving http: ", url)

json_handle = urllib.request.urlopen(url, context=ctx)
json_data = json_handle.read().decode()
print("Retrieved ", len(json_data), " characters")

content = json.loads(json_data)

plus_code = (json.dumps(content["features"][0]["properties"]["plus_code"]))
plus_code = plus_code.strip('"')

print(plus_code)
