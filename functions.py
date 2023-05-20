import requests

def full_city_json(url):
    return requests.get(url).json()

def get_coordinates(url):
    lat = url["coord"]["lat"]
    lon = url["coord"]["lat"]
    return lat, lon

def get_temperature(url):
    temp = url["main"]["temp"]
    temp_min= url["main"]["temp_min"]
    temp_max= url["main"]["temp_max"]
    return temp, temp_min, temp_max

def get_feels(url):
    feels_like = url["main"]["feels_like"]
    humidity = url["main"]["humidity"]
    pressure = url["main"]["pressure"]
    return feels_like, humidity, pressure

def city_and_country_names(url):
    city = url["name"]
    country = url["sys"]["country"]
    return city, country

def get_weather_description(url):
    description = url["weather"][0]["description"]
    icon = url["weather"][0]["icon"]
    return description, icon