import requests
from datetime import datetime
import data_file
from website3 import data2


def data1():
    try:  # To verify the valid city name or not
        date = datetime.now().date()
        time = datetime.now().time().strftime("%H:%M:%S")
        Location_name = input("Enter the Location name: ")
        apikey = "d3fafd168743c2c86c90977cb8babb03"
        url = f'https://api.openweathermap.org/data/2.5/weather?q={Location_name}&appid={apikey}'
        res = requests.get(url)
        data = res.json()  # To convert the retrieved data into JSON format
        temp = (round(data['main']['temp'] - 272.15))
        wind_speed = data['wind']['speed']
        Sky_Description = data['weather'][0]['description']
        weather = data['weather'][0]['main']
        print(f"Searching...for weather in {Location_name}\n")

        # To print the result on word file
        data_file.doc.add_paragraph(
            f'Date: {date}\nTime: {time}\nWeather: {weather}\nTemperature: {temp}°C\n'
            f'Wind Speed: {wind_speed}\nSky_Description: {Sky_Description}')
        choice = input("Do you want to search for weather in another location? Yes/No: ").lower()
        if choice in ['yes', 'y']:
            data2()
        else:
            data_file.file()
    except KeyError:
        print("City name name not found...\nTry again..")
        data_file.file()

# website1()
