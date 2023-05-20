from pprint import pprint
import functions as func
from env import open_weather_map_api_key as key










if __name__ == "__main__":

    print("~~~~~~ Welsome to 24 Weather Cast ~~~~~~")
    city_name = input("Enter a city name: ")
    city_name = city_name.replace(" ", "%20") # replace empty space if contained in city input
    
    # api request url
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key()}"
    # pprint(func.full_city_json(url))
    


    


    # user_preview = input("How would like your forcast? (Celsius 'C' or Fehrenheit 'F')\n")

    



    dic = {'base': 'stations',
            'clouds': {'all': 100},
            'cod': 200,
            'coord': {'lat': 42.9634, 'lon': -85.6681},
            'dt': 1684588302,
            'id': 4994358,
            'main': {'feels_like': 279.4,
                    'humidity': 88,
                    'pressure': 1017,
                    'temp': 282.12,
                    'temp_max': 282.84,
                    'temp_min': 281.33},
            'name': 'Grand Rapids',
            'sys': {'country': 'US',
                    'id': 2005020,
                    'sunrise': 1684577705,
                    'sunset': 1684631015,
                    'type': 2},
            'timezone': -14400,
            'visibility': 10000,
            'weather': [{'description': 'overcast clouds',
                        'icon': '04d',
                        'id': 804,
                        'main': 'Clouds'}],
            'wind': {'deg': 280, 'speed': 5.14}}
    

    print(func.get_feels(dic))