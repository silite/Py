import urllib.request
response = urllib.request.urlopen("http://lilun.cfjiakao.com/student/Main.js")
s = response.read()

print(s)
with open('s.js', 'wb') as f:

	f.write(s)