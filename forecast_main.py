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
                feels_like, humidity, humidity_description,pressure,
                city, country,
                description, icon, main,
                degree, speed,
                visibility, wind_direction,
                visibility_categories,
                sunrise, sunset
                ):
    """
    Parameters:
        ¿¿¿ All weather data functions ¿¿¿
            lat, lon, 
            temp, temp_min, temp_max,
            feels_like, humidity, humidity_description, pressure,
            city, country,
            description, icon, main,
            degree, speed,
            visibility, wind_direction,
            visibility_categories,
            sunrise, sunset
    Returns:
        Paragraph string describing the current weather forcust
    """
    name = "Victoire Migashane"
    email_message = f"""Good morning {name}! Here's your daily python weather forecast for {city}:\n\n\
Today, the weather in {city} is mostly {main} with {description}. The temperature is currently around {temp} Celsius, \
with a maximum of {temp_max} Celsius, and a minimum of {temp_min} Celsius. \n\nToday's feels like temperature is {feels_like} Celsius. \
The humidity is relatively {humidity_description} at {humidity}%, and the atmospheric pressure is {pressure} hPa. \
The wind is blowing from the {wind_direction} at a speed of {speed} meters per second, with a direction of {degree} degrees. Visibility \
is {visibility_categories}, reaching {visibility} meters. The sunrise was at the local time of {sunrise} AM, \
and the sunset is expected to occur at {sunset} PM. \n\nEnjoy your day in {city}, and don't forget to dress accordingly for the {description} conditions."""
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
        feels_like, humidity, humidity_description, pressure= func.get_feels(curr_data())
        city, country = func.city_and_country_names(curr_data())
        description, icon, main = func.get_weather_description(curr_data())
        degree, speed = func.get_wind(curr_data())
        visibility = func.get_visibility(curr_data())
        sunrise, sunset = func.get_sunset_sunrise(curr_data())

        wind_direction = func.compass(degree)
        visibility_categories = func.get_visibility_options(visibility)

        # Convert temperature from kelvin to celsius
        temp, temp_min, temp_max = func.kelvin_to_celsius(temp), func.kelvin_to_celsius(temp_min), func.kelvin_to_celsius(temp_max)
        feels_like = func.kelvin_to_celsius(feels_like)

        # Full weather forecast message
        email_message = email_propt(lat, lon, 
                    temp, temp_min, temp_max,
                    feels_like, humidity, humidity_description,pressure,
                    city, country,
                    description, icon, main,
                    degree, speed,
                    visibility, wind_direction,
                    visibility_categories,
                    sunrise, sunset
                    )
        func.mac_speak(email_message)

        # func.connect_email(email, password, email_message)
        break