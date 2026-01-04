from urllib import request, error, parse
import requests
# from urllib import url

def download(url, retries = 3):
    req = request.Request(url)
    try:
        resp = request.urlopen(req)
    except error.HTTPError as e:
        if 400 <= e.getcode() < 500 or retries < 1:
            resp = None
        elif 500 <= e.getcode() < 600:
            resp = download(url, retries - 1)
            print("retry :", retries)
    return resp
# headers = {'user-agent':'Mozilla/5.0'}
# resp = download("https://www.crawler-test.com/status_codes/status_500")
url = "https://www.google.com/search?q=%ED%81%AC%EB%A1%A4%EB%A7%81&oq=%ED%81%AC%EB%A1%A4%EB%A7%81&gs_lcrp=EgZjaHJvbWUyDAgAEEUYORixAxiABDIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCTQ2MTVqMGoxNagCCLACAfEFEqR69VmHRxHxBRKkevVZh0cR&sourceid=chrome&ie=UTF-8"

componets = parse.urlparse(url)
qs = parse.parse_qs(componets.query)
print("before Query :", qs)
qs["q"] = "NLP"
parse.urlencode(qs)
print("after Query :", qs)
print(componets)
print("#######################")
params = {'q':"자연어 처리"}
strURL = parse.urljoin(url, parse.urlparse(url).path + "?" + parse.urlencode(params))
print(strURL)
print(parse.urlencode({'q':url}))

pe = parse.quote(params['q'])
pe_plus = parse.quote_plus(params['q'])
print(pe)
print(pe_plus)
print(parse.unquote(pe))
print(parse.unquote_plus(pe_plus))


peUtf = parse.quote(params['q'])
peEuc = parse.quote(params['q'], encoding="EUC-KR")
print(peUtf, "/", peEuc)
print(parse.unquote(peUtf), "/", parse.unquote(peEuc))
# get method
url = "http://httpbin.org/get?" + parse.urlencode({'key':"value"})
req = request.Request(url)
resp = request.urlopen(req)
print(resp.read())
# post method
url = "http://httpbin.org/post"
req = request.Request(url, parse.urlencode({'key':"value"}).encode())
resp = request.urlopen(req)
print(resp.read())

def postDownload(url, data = None, retries = 3):
    print("################### postDownload #################")
    resp = None #;   header = {'user-agent': 'Mozilla/5.0'}
    try:
        resp = requests.post(url, data = data)#, headers = header)
        print("postDownload{0} ::".format(data), resp)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if 500 <= e.getcode() < 600 and retries > 0:
            print("Retries : {0}".format(retries))
            return postDownload(url, data, retries-1)
        else:
            print(resp.status.code)
            print(resp.reson)
            print(resp.request.headers)
    return resp

def cookieDownload(url, data = None, cookie = None, retries = 3):
    resp = None #;   header = {'user-agent': 'Mozilla/5.0'}
    try:
        resp = request.post(url, data = data) #, headers = header)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if 500 <= e.getcode() < 600 and retries > 0:
            print("Retries : {0}".format(retries))
            return postDownload(url, data, cookie, retries-1)
        else:
            print(resp.status.code)
            print(resp.reson)
            print(resp.request.headers)
    return resp

url = "http://pythonscraping.com/pages/cookies/welcome.php"
data = {'username':'test', 'password':'password'}
html = postDownload(url, data)
print("not cookie :\n", html.text)
cookie = html.cookies.get_dict()
print("cookie info :", cookie)
html = requests.post(url, cookies=cookie)
print("cookie :\n", html.text)