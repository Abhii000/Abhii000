import requests,os,time
from colorama import Fore

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # You can change units to "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    #print(response.text)  # Print the API response for debugging purposes
    
    try:
        

        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        feels_like=data['main']['feels_like']
        min_temp=data['main']['temp_min']
        max_temp=data['main']['temp_max']
        pressure_atm=data['main']['pressure']
        wind_speed=data['wind']['speed']


        print(Fore.CYAN+f"Weather in {city}: {weather_description}")
        print(Fore.LIGHTCYAN_EX+f"Temperature: {temperature}°C")
        print(Fore.LIGHTGREEN_EX+'Feels like: ',feels_like)
        print(Fore.YELLOW+f"Humidity gm/m3: {humidity}%")
        print(Fore.LIGHTRED_EX+'Min Temperature in Celcious: ',min_temp)
        print(Fore.RED+'Max Temperature in Celcious: ',max_temp)
        print(Fore.MAGENTA+'Pressure in hPa: ',pressure_atm,Fore.WHITE+'')
        print(Fore.BLUE+'Wind Avg Speed in kmph: ',wind_speed)

        print('\nExtra Info:-\n')
        for data_1 in data:
            print(data_1,' : ',data[f'{data_1}'])
            time.sleep(0.03)
        print(Fore.CYAN+'')


        
            
                
               

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

if __name__ == "__main__":
    city_name = input(Fore.BLUE+"Name of city: ")
    api_key = "0d0ead0cdd38d1765871b6757510a2ee"  # Replace with your actual API key
    get_weather(city_name, api_key)
