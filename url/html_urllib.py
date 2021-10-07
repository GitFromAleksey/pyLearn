import urllib.request
import requests


##print(urllib)
##print(dir(urllib))
##print(urllib.__file__)

##url = 'https://vk.com'
url = 'http://192.168.1.1'
##url = 'http://192.168.1.1/index.cgi'

##ul = urllib.request.urlopen(url)
##print()
##for l in ul.readlines():
##    print(l)
##
##for h in ul.getheaders():
##    print('h:\n',h)
##print('raw data:')
##with urllib.request.urlopen(url) as f:
##    print(f.read(300))

req = urllib.request.Request(url)
##req.add_header
passman = urllib.request.urlunparse

url_content = urllib.request.urlopen(url)
data = url_content.getcode()
print('{data:}',data)
content = url_content.read()

html = content.decode('utf-8')
start_idx = html.find('<a href=')
print(html[start_idx : start_idx+50])

print('utf-8 data:')
file_content = open('content.html','bw')
file_content.write(content)#.decode('utf-8'))
file_content.close()                                    
print(content)
