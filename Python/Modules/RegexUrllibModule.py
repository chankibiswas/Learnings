import urllib.request
import urllib.parse

url = "http://pythonprogramming.net"
values = {'s':'basic','submit':'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)

respdata = resp.read()

import re

paragraphs = re.findall(r'<p>(.*?)</p>', str(respdata))

for para in paragraphs:
    print(para)
