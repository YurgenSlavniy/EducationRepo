# e5e4cd692a72b0b66ea0a6b80255d1c3
import requests
from pprint import pprint

params = {'q': 'Samara',
          'appid': 'e5e4cd692a72b0b66ea0a6b80255d1c3'}
url = "https://api.openweathermap.org/data/2.5/weather"
response = requests.get(url, params=params)
j_data = response.json()
# print(type(j_data))
# pprint(j_data)

print(f"В городе {j_data['name']} температура {round(j_data['main']['temp'] - 273.15, 2)} градусов")


