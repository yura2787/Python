import requests

url = 'https://dummyjson.com/users'

params = {
    'limit': 1000,
    'skip': 0
}

response = requests.get(url, params=params)
response_json = response.json()

users = response_json['users']

the_number_of_users_younger_than_30_years = 0
how_many_women_with_green_eyes = 0
how_many_people_live_in_san_francisco = 0

for user in users:
    if user['age'] < 30:
        the_number_of_users_younger_than_30_years += 1

    if user['gender'] == 'female' and user['eyeColor'] == 'Green':
        how_many_women_with_green_eyes += 1

    if user['address']['city'] == 'San Francisco':
        how_many_people_live_in_san_francisco += 1
