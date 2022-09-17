# Beautiful soup is a Python library used to extract data from HTML and XML files i.e for web scraping purpose
# Used Python's requests module to make HTTP requests

from bs4 import BeautifulSoup
import requests

import data_file


def weather_data():
    try:  # To verify the valid city name or not
        city_name = input("Enter the city name: ")
        city = city_name + "weather"
        headers = {  # headers contain protocol-specific information
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(
            f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
            headers=headers)  # Passing google search to the get function to retrieve weather data

        print(f"Searching...for weather in {city_name}\n")
        soup = BeautifulSoup(response.text, 'html.parser')
        location = soup.select('#wob_loc')[0].getText().strip()
        time = soup.select('#wob_dts')[0].getText().strip()
        information = soup.select('#wob_dc')[0].getText().strip()
        weather = soup.select('#wob_tm')[0].getText().strip()
        humidity = soup.select('#wob_hm')[0].getText().strip()
        wind_speed = soup.select('#wob_ws')[0].getText().strip()
        precipitation = soup.select('#wob_pp')[0].getText().strip()

        return {
            "location": location,
            "time": time,
            "information": information,
            "weather": weather,
            "humidity": humidity,
            "wind_speed": wind_speed,
            "Precipitation": precipitation
        }
    except IndexError:
        print("City name not found....")
        data_file.file()


# weather_data()
