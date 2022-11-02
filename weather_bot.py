import requests

API_KEY = "e9ee9f5ca50573b8b7350ed88a282cf8"
BASE_URL = "https://openweathermap.org/data/2.5/weather/"

city  = input('Enter a city name: ')
request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('An error occured')