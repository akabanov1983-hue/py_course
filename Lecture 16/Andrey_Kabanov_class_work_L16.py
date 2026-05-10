import requests

url = "https://jsonplaceholder.typicode.com/todos/"
res = requests.get(url)
print(res)
print(res.status_code)
print(res.json())
print(res.text)

data = {'userId': 1, 'id': 2, 'title': 'delectusdsdsdsdsd aut autem', 'completed': False}

resp = requests.post(url, json=data)
print(resp.status_code)


data = {'userId': 2, 'id': 1000, 'title': 'fefweerewrwer', 'completed': True}

resp = requests.post(url, json=data)

print(resp.status_code)

key = "DEMO_KEY"

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"

p = {"api_key": key, "earth_date":""}