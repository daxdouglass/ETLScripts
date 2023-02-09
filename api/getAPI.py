import requests

response = requests.get('https://randomuser.me/api/')

title = response.json()['results'][0]['name']['title']

first_name = response.json()['results'][0]['name']['first']

last_name = response.json()['results'][0]['name']['last']

gender = response.json()['results'][0]['gender']

age = response.json()['results'][0]['dob']['age']

print(f'{title}. {first_name} {last_name}')
print(f' Gender: {gender}')
print(f' Age: {age}')
