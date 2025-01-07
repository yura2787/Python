import requests

url = 'http://api.open-notify.org/astros.json'

params = {}

response = requests.get(url, params=params)
response_json = response.json()
peoples = response_json['people']

name_people_iss = []

for people in peoples:
    if people['craft'] == 'ISS':
        name_people_iss.append(people['name'])

print(name_people_iss)
