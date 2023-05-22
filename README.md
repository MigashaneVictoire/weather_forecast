# Python Weather Forecast 

This Python script retrieves the current weather forecast for a specified city using the OpenWeatherMap API. It obtains weather data such as temperature, humidity, wind speed, visibility, and sunrise/sunset times. The script also includes functionality to send the weather forecast via email.

## Installation

To run the script, you need to install the required dependencies. Use the following command to install the necessary packages:

```
pip install requests
```

Make sure you have a valid API key from OpenWeatherMap and valid email credentials before running the script.

## Usage

The script consists of two files: `main.py` and `functions.py`. The `main.py` file contains the main program logic, while the `functions.py` file provides various functions to retrieve and process weather data.

Before running the script, make sure to set up your API key and email credentials in the env.py file. Replace the placeholders with your actual values.

```
# env.py

def open_weather_map_api_key():
    return "YOUR_API_KEY"

def email_credentials():
    return "YOUR_EMAIL", "YOUR_PASSWORD"
```

To use the script, execute the `main.py` file. It will provide you with a daily weather forecast for the default city (San Antonio). If you want to get the forecast for a different city, or name of user, uncomment the line in the script that prompts for user input and enter the desired `city_name` and change `name`.

```
# Program will run starting here
if __name__ == "__main__":
    while True:
        # ...
        name = "YOUR_NAME"

        # set default city because I want daily emails with no questions
        city_name = "San Antonio"
        # city_name = input("Enter a city name: ")  # uncomment to use a different city
        # ...

        break
```

The script will print the weather forecast information and read it aloud using the text-to-speech functionality available on macOS. Additionally, it includes a commented-out function `connect_email` to send the weather forecast via email. Uncomment and fill in the required email details to enable this functionality.

## Available Functions
The `functions.py` file provides the following functions:

* `full_curr_city_json(url)`: Makes an API call to retrieve the current weather data for a specific city.
* `get_coordinates(data)`: Extracts latitude and longitude from the weather data.
* `get_temperature(data)`: Retrieves the current temperature, minimum temperature, and maximum temperature.
* `get_feels(data)`: Retrieves the "feels like" temperature, humidity, humidity description, and pressure.
* `city_and_country_names(data)`: Retrieves the name of the city and country.
* `get_weather_description(data)`: Retrieves the weather description, icon image code, and main forecast.
* `get_wind(data)`: Retrieves the wind direction and speed.
* `get_visibility(data)`: Retrieves the visibility in meters.
* `get_sunset_sunrise(data)`: Retrieves the sunrise and sunset times.
* `mac_speak(message)`: Reads a message aloud using macOS's text-to-speech functionality.
* `kelvin_to_celsius(kelvin)`: Converts a temperature value from Kelvin to Celsius.
* `compass(degree)`: Converts a wind direction in degrees to a corresponding compass direction.
* `get_visibility_options(visibility)`: Categorizes the visibility based on the provided value.
* `connect_email(sender_email, passCode, message)`: Sends an email with the specified sender email, password, and message.

These functions are used to extract and process the weather data in the `main.py` script.

## Contributing
Feel free to contribute to the project by submitting issues or pull requests on the GitHub repository.