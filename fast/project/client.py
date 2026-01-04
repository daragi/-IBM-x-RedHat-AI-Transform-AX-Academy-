import requests

res1 = requests.get("http://localhost:8000") # localhost:8000이 이미 먹혀있음
res2 = requests.get("http://localhost:8000/items/10?q=hello")
res_json1 = res1.text
res_json2 = res2.json()

print(res_json1)
print(res_json2)