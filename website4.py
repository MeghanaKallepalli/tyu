import requests
from datetime import datetime
import data_file
from website5 import data4


def data3():
    def weather(result, city):
        from datetime import date, timedelta
        tomorrow = date.today() + timedelta(days=1)
        day_after_tmr = date.today() + timedelta(days=2)
        time = datetime.now().strftime("%H:%M:%S")
        date = datetime.now()
        a = ("Today {}'s Temperature is: {}".format(city, result["temperature"]))
        b = ("Wind speed is: {}".format(result["wind"]))
        c = ("climate condition is: {}".format(result["description"]))
        e = ("{} temperature is: {}".format(tomorrow, result["forecast"][0]["temperature"]))
        f = ("wind speed is: {}".format(result["forecast"][0]["wind"]))
        h = ("{} temperature is: {}".format(day_after_tmr, result["forecast"][0]["temperature"]))
        i = ("wind speed is: {}".format(result["forecast"][0]["wind"]))
        print(f"Searching...for weather in {city}\n")
        # To print the result on word file
        data_file.doc.add_paragraph(
            "\n" + f' Date : {date}  \n Time : {time}  \n Location : {city} \n + {a} \n {b} \n {c} \n {e} \n {f} \n {h} \n {i}\n')
        choice = input("Do you want to search for weather in another location? Yes/No: ").lower()
        if choice in ['yes', 'y']:
            data4()
        else:
            data_file.file()

    def weather_data(query):
        url = requests.get(f"https://goweather.herokuapp.com/weather/%7Bquery%7D%22")
        return url.json()

    def main():
        city = input("enter your city name: ")
        try:  # To verify the valid city name or not
            query = 'q=' + city
            w_data = weather_data(query)
            weather(w_data, city)
        except:
            print('City name not found...\nTry again..')
            data_file.file()


    main()
# data()
