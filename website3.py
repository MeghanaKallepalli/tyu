import requests
import data_file
from website4 import data3


def data2():
    try:  # To verify the valid city name or not
        citydata = input('Enter city name: ')
        print(citydata)
        url = 'https://wttr.in/{}?format="Location:%l\nWeather condition:%c\nTemperature:%t\nMoon phase:%m\nWeather:%C\n' \
              'Humidity:%h\nTemp feels like:%h\nWind:%w\nMoon day:%M\nPrecipitation:%p\nPressure:P\nUV index:%u"'.format(
            citydata)
        res = requests.get(url)
        print(f"Searching...for weather in {citydata}\n")
        data_file.doc.add_paragraph(res.text)  # To print the result on word file
        choice = input("Do you want to search for weather in another location? Yes/No: ").lower()
        if choice in ['yes', 'y']:
            data3()
        else:
            data_file.file()
    except:
        print("City name not found...\nTry again..")
        data_file.file()


# website2()
