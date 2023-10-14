import requests
security_point = 0
url = 'http://testphp.vulnweb.com/'
response = requests.get(url,timeout=5)
headers = response.headers
key,value = [],[]
geninfo = []
for k,v in headers.items():
    key.append(k)
    value.append(v)
if "Server" in key:
    if  any(map(str.isdigit, headers["Server"])):
        geninfo.append(headers['Server'])
if "X-Powered-By" in key:
    geninfo.append(headers['X-Powered-By'])
headers = '''X-Content-Type-Options
Content-Security-Policy
Strict-Transport-Security
X-Frame-Options
Referrer-Policy'''.split()
missing = []
print(f"#{'-'*50}")
for header in headers:
    if header not in key:
        missing.append(header)
if len(headers)>0:
    print("The following security header are missing:")
    for m in missing:
        print(f" - {m}")
else:   print("There no missing HTTP security header.\n Good job!")
if len(geninfo)>0:
    print("The attacker can gain the following information from HTTP response:")
    for g in geninfo:
        print(f" - {g}")