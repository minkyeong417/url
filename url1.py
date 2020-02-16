def goto18(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    count = 0
    tags = soup('a')
    for tag in tags:
        count = count + 1
        if count == 18:
            print (tag.get('href',None))
            return tag.get('href', None)

            break

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

for i in [1,2,3,4,5,6,7]:
    url = goto18(url)
# Retrieve all of the anchor tags
