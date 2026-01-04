import requests

url = "http://pythonscraping.com/pages/cookies/welcome.php"
data = {'username': 'test', 'password': 'password'}

# 세션 객체 생성
session = requests.Session()

# 로그인(POST) 요청
response = requests.get(url, params=data)
print("not cookie :\n", response.text)

# 세션에 저장된 쿠키 확인
cookie = session.cookies.get_dict()
print("cookie info :", cookie)

# 쿠키를 포함해서 다시 요청
response2 = session.get(url)
print("cookie :\n", response2.text)