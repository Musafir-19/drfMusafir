import requests

url = 'http://127.0.0.1:8000/api/v1/posts/'

res = requests.get(url)
print(res.text)