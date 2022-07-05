import requests
from config import key

def temperature(city_name):
    try:
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}')
        total = response.json()
        kelvin = total['main']['temp']
        temp = int(kelvin - 273)
        return temp
    except:
        return False
while True:
    city_name = input('Введите город: ')
    if temperature(city_name):
        print(f'Температура в городе {city_name}: {temperature(city_name)}')
    else:
        print('Введите корректно город')
