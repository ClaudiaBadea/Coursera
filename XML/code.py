import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import ssl

total = 0
url = input('Enter location: ')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)

results = tree.findall('comments/comment')
for comment in results:
    num = comment.find('count').text
    fnum = float(num)
    total = total + fnum
print(total)
