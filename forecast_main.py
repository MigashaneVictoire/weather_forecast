import requests
import keys













if __name__ == "__main__":
    agro_monitor_key = keys.agro_monitoring_api_key()
    open_weather_key = keys.open_weather_map_api_key()

    print("~~~~~~ Welsome to 24 Weather Cast ~~~~~~")
    city_name = input("Enter the city: ")
    city = city_name.replace(" ", "%20") # replace empty space if contained in city input
    
    # api request url
    city_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={open_weather_key}"

    print(requests.get(city_url).json())
    # user_preview = input("How would like your forcast? (Celsius 'C' or Fehrenheit 'F')\n")

    