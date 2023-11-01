import requests
import optparse

def get_url_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-u', '--url', dest='url', help='URL to check')
    (options, args) = parser.parse_args()
    return options.url

url = get_url_arguments()
if url is None:
    print("Please provide a URL using the -u option.")
else:
    security_point = 0
    response = requests.get(url, timeout=5)
    headers = response.headers
    key, value = [], []
    geninfo = []
    for k, v in headers.items():
        key.append(k)
        value.append(v)
    if "Server" in key:
        if any(map(str.isdigit, headers["Server"])):
            geninfo.append(headers['Server'])
    if "X-Powered-By" in key:
        geninfo.append(headers['X-Powered-By'])
    headers = '''X-Content-Type-Options
    Content-Security-Policy
    Strict-Transport-Security
    X-Frame-Options
    Referrer-Policy'''.split()
    missing = []
    print(f"#{'-' * 50}")
    for header in headers:
        if header not in key:
            missing.append(header)
    if len(headers) > 0:
        print("The following security headers are missing:")
        for m in missing:
            print(f" - {m}")
    else:
        print("There are no missing HTTP security headers.\n Good job!")
    if len(geninfo) > 0:
        print("The attacker can gain the following information from the HTTP response:")
        for g in geninfo:
            print(f" - {g}") #teest
