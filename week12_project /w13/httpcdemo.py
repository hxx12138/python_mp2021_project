import http.client
import sys
import urllib.parse

#get
'''conn = http.client.HTTPConnection(sys.argv[1])
conn.request("GET", "/")
r1 = con.getresponse()
print("status",end=':')
print(r1.status)
print('-'*50)
print("reason",end=':')
print(r1.reason)
print('-'*50)
print("info")
print(r1.info())
conn.close()
'''

#post
'''params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
conn = http.client.HTTPConnection("bugs.python.org")
conn.request("POST", "", params, headers)
response = conn.getresponse()
print(response.status, response.reason)
data = response.read()
print(data)
conn.close()'''

