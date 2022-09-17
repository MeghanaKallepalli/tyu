import requests
import data_file


def data4():
    from Weather_Forecasting import weather
    try:  # To verify the valid city name or not
        citydata = input('Enter city name: ')
        apikey = "cd7f1f7700bf425898828fd7864a7813"
        url = 'https://api.weatherbit.io/v2.0/current?'
        url1 = url + "&Key=" + apikey + "&City=" + citydata
        res3 = requests.get(url1)
        data3 = res3.json()
        temperature = (data3['data'][0]['temp'])
        wind_dir = (data3['data'][0]['wind_cdir_full'])
        description = (data3['data'][0]['weather']['description'])
        sunset = (data3['data'][0]['sunset'])
        print(f"Searching...for weather in {citydata}\n")
        # To print the result on word file
        data_file.doc.add_paragraph(f"{temperature} \n {wind_dir} \n {description} \n {sunset}")
        choice = input("Do you want to search for weather in another location? Yes/No: ").lower()
        if choice in ['yes', 'y']:
            weather()
        else:
            data_file.file()
    except:
        print("City name not found...\nTry again..")
        data_file.file()


# website5()
