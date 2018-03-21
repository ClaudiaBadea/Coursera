import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

total = 0
url = input('Enter location: ')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen(url)
data = uh.read()

info = json.loads(data)

for item in info['comments']:
    number = item['count']
    total = total + number
print(total)
