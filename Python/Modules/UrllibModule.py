import urllib.request
import urllib.parse

'''
url = urllib.request.urlopen("http://cartopia-rmds.tomtomgroup.com/cartopia/configs/application-context.xml")
print(url.read)
'''

'''
url = "http://pythonprogramming.net"
values = {'s':'basic','submit':'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)

print(resp.read())
'''

'''
try:
    req = urllib.request.urlopen("http://www.google.com/search?q=test")
    print(req.read())
except Exception as e:
    print(e)
'''

try:
    url = "http://www.google.com/search?q=test"
    headers = {"User-Agent":"Chrome/24.0.1312.27"}
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    #print(resp.read())

    savefile = open('googleResponce.txt','w')
    savefile.write(str(resp.read()))
    savefile.close()
except Exception as e:
    print(e)







    
