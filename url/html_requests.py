import requests

##url = 'http://192.168.1.1'
url = 'http://192.168.1.1/index.cgi'

values = {'usernsme' : 'admin',
          'password' : 'admin1'}

r = requests.post(url, data = values)

print(r)

print(r.cookies)
print(r.encoding)
print(r.headers)
print(r.json)
print(r.links)
print(r.next)
print(r.ok)
print(r.raw)
print(r.reason)
print(r.request)
print(r.url)

print(r.text)
##print(r.content)
