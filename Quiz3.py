import requests

response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=API_KEY')

status_code = response.status_code

headers = response.headers

print(f"Status Code: {status_code}")
print("Headers:")
for key, value in headers.items():
    print(f"{key}: {value}")

import json

data = response.json()

with open('weather_data.json', 'w') as file:
    json.dump(data, file, indent=4)


city = data['name']
temperature = data['main']['temp']
description = data['weather'][0]['description']

print(f"City: {city}")
print(f"Temperature: {temperature} K")
print(f"Description: {description}")

import sqlite3


conn = sqlite3.connect('weather.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather_data (
        city TEXT,
        temperature REAL,
        description TEXT
    )
''')

cursor.execute('''
    INSERT INTO weather_data (city, temperature, description)
    VALUES (?, ?, ?)
''', (city, temperature, description))

conn.commit()
conn.close()

