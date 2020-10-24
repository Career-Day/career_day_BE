import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 10, "name": "tim", "views": 100},
        {"likes": 15, "name": "joe", "views": 140},
        {"likes": 19, "name": "bob", "views": 50}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

response = requests.patch(BASE + "video/2")

input()
response = requests.get(BASE + "video/6")
print(response.json())
