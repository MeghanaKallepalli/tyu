"""Forecasting of weather involves recording the ongoing measurements
               of temperature, pressure, precipitation,
            wind speed and the amount of cloud cover and
      giving those current recordings and reports to the public..."""

from website2 import data1
import data_file


def weather():  # To run the loop till user want to quit
    data_file.data()
    choice = input("Do you want to search for weather in another location? Yes/No: ").lower()
    if choice in ["yes", "y"]:
        data1()
    else:
        data_file.file()


weather()
