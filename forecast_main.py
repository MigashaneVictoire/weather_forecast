from pprint import pprint
import functions as func
import env


def curr_data():
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
    return dic

def email_propt(lat, lon, 
                temp, temp_min, temp_max,
                feels_like, humidity, pressure,
                city, country,
                description, icon,
                degree, speed,
                visibility
                ):
    """
    Parameters:
        ¿¿¿ All weather data functions ¿¿¿
            lat, lon, 
            temp, temp_min, temp_max,
            feels_like, humidity, pressure,
            city, country,
            description, icon,
            degree, speed,
            visibility
    Returns:
        Paragraph string describing the current weather forcust
    """
    email_message = f"The current weather in {city}, located at latitude {lat} and longitude {lon}, \
is characterized by {description}. The temperature is {temp} Celsius, with a maximum of {temp_max} Celsius, \
and a minimum of {temp_min} Celsius. The humidity level is at {humidity}%, and the atmospheric pressure is {pressure} hPa. \
The wind is blowing at a speed of {speed} meters per second, from a direction of {degree} degrees. The visibility is \
excellent at {visibility} meters. The weather condition is represented by the presence of {description}. \
The weather code is 804, indicating the cloudiness. The sunrise occurred at 1684577705 seconds \
since the Unix epoch, while the sunset is expected to happen at 1684631015 seconds. {city} \
is located in the {country}, and the local time zone is Eastern Daylight Time."
    return email_message


# Program will run starting here
if __name__ == "__main__":
    while True:
    # get cridentials
        api_key = env.open_weather_map_api_key()
        email, password = env.email_cridentials()

        print("~~~~~~ Welsome to 24 Weather Cast ~~~~~~")

        # set default city beause I want dayly emails with no questions
        city_name = "San Antonio"
        # city_name = input("Enter a city name: ")  # uncomment to use different city
        city_name = city_name.replace(" ", "%20") # replace empty space if contained in city input

        # api request link
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
        # data = func.full_curr_city_json(url)

        # All weather function call re-assignment
        lat, lon = func.get_coordinates(curr_data())
        temp, temp_min, temp_max = func.get_temperature(curr_data())
        feels_like, humidity, pressure= func.get_feels(curr_data())
        city, country = func.city_and_country_names(curr_data())
        description, icon = func.get_weather_description(curr_data())
        degree, speed = func.get_wind(curr_data())
        visibility = func.get_visibility(curr_data())

        # Convert temperature from kelvin to celsius
        temp, temp_min, temp_max = kelvin_to_celsius(temp), kelvin_to_celsius(temp_min), kelvin_to_celsius(temp_max)


        # Full weather forecast message
        email_message = email_propt(lat, lon, 
                    temp, temp_min, temp_max,
                    feels_like, humidity, pressure,
                    city, country,
                    description, icon,
                    degree, speed,
                    visibility
                    )
        # func.mac_speak(email_message)

        # func.connect_email(email, password, email_message)
        break