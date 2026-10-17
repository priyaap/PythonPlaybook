import urllib.request, urllib.parse, urllib.error
import ssl
import re
import xml.etree.cElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# data = '''
# <commentinfo>
#     <note>This file contains the sample data for testing</note>
#     <comments>
#         <comment>
#             <name>Romina</name>
#             <count>97</count>
#         </comment>
#     </comments>
# </commentinfo>'''

url = 'http://py4e-data.dr-chuck.net/comments_2267532.xml'

content = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(content)

#count_list = tree.findall('./comments/comment/count')
count_list = tree.findall('.//count')
count_sum = 0

for count in count_list:
    count_sum = count_sum + int(count.text)

print("ANSWER: ", count_sum)