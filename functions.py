import requests

# api call
def full_curr_city_json(url) -> str:
    """
    Parameters:
        url: string containing city name and api key for requests
    Returns:
        current weather json data from openweathermap.org
    """
    return requests.get(url).json()

# coordinates data
def get_coordinates(data) -> dict:
    """
    Parameters:
        data: json data from api call
    Returns:
        latitude and longitude of current city
    """
    lat = data["coord"]["lat"]
    lon = data["coord"]["lat"]
    return lat, lon

# get temperature data
def get_temperature(data) -> dict:
    """
    Parameters:
        data: json data from api call
    Returns:
        current temperature, minimum temperature and maximum teperature
    """
    temp = data["main"]["temp"]
    temp_min= data["main"]["temp_min"]
    temp_max= data["main"]["temp_max"]
    return temp, temp_min, temp_max

# get additional temp data
def get_feels(data) -> dict:
    """
    Parameters:
        data: json data from api call
    Returns:
        outdoors feel, himidity and pressure
    """
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    return feels_like, humidity, pressure

# get country and city names
def city_and_country_names(data) -> dict:
    """
    Parameters:
        data: json data from api call
    Returns:
        name of city and name of country
    """
    city = data["name"]
    country = data["sys"]["country"]
    return city, country

# describe current weather
def get_weather_description(data) -> dict:
    """
    Parameters:
        data: json data from api call
    Returns:
        weather discription and icon image code
    """
    description = data["weather"][0]["description"]
    icon = data["weather"][0]["icon"]
    return description, icon
    # note: could add some NLP to show clodiness responces

# wind description data
def get_wind(data) -> dict:
    """
    Parameters:
        data: json data from api call
    Returns:
        wind direction and wind speed
    """
    degree = data["wind"]["deg"]
    speed = data["wind"]["speed"]
    return degree, speed

# get view data
def get_visibility(data) -> dict:
    """
    Parameters:
        data: json data from api call
    Returns:
        out doors visibility
    """
    visibility = data["visibility"]
    return visibility
