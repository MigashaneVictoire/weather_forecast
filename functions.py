import requests
from datetime import datetime
import numpy as np
import os

# send email importsi
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Main weather functios
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
        outdoors feel, himidity , humidity_description, and pressure
    """
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    humidity_description = ""
    pressure = data["main"]["pressure"]

    # humidity description
    if humidity < 35:
        humidity_description = "low"
    elif humidity > 75:
        humidity_description = "high"
    else:
        humidity_description = "fair"

    return feels_like, humidity, humidity_description, pressure

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
        weather discription, icon image code, and main forecasts to the day
    """
    description = data["weather"][0]["description"]
    icon = data["weather"][0]["icon"]
    main = data["weather"][0]["main"]
    return description, icon, main
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

def get_sunset_sunrise(data):
    """
    Parameters:
        data: json data from api call
    Returns:
        sunrise: hour and minute for the sun rise
        sunset: hour and minute for the sun set
    """
    sunrise = data["sys"]["sunrise"]
    sunset = data["sys"]["sunset"]

    # Convert seconds to datetime string
    sunrise = datetime.utcfromtimestamp(sunrise).strftime('%Y-%m-%d %H:%M:%S')
    sunset = datetime.utcfromtimestamp(sunset).strftime('%Y-%m-%d %H:%M:%S')

    # Restracture datetime to just time
    sunrise = sunrise.split()[1][:-3]
    sunset = sunset.split()[1][:-3]

    return sunrise, sunset #datetime.time(sunrise), datetime.time(sunset)

# other functions
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# get sound from mac
def mac_speak(message) -> str:
    """
    Parameters:
        message: Weather forcast message to be read by os
    returns:
        Sound, reading the message
    """
    os.system(f"say {message}")

# Convert temp from kelvin to celsius
def kelvin_to_celsius(kelvin) -> float:
    """
    Parameters:
        kelvin: float temp value to be converted
    returns:
        degrees in celsius
    """
    celsius = kelvin - 273.15
    return round(celsius, 2)

# categorize compass
def compass(degree) -> int or float:
    """
    Parameters:
        degree: direction of wind in degrees
    returns:
        corresponding wind direction from based on compass
    """
    # north
    if degree >= 337.5 or degree >= 0.0 and degree < 22.5:
        return "north"
    #north east
    elif degree >= 22.5 and degree < 67.5:
        return "north east"
    
    # east
    elif degree >= 67.5 and degree < 112.5:
        return "east"
    # south east
    elif degree >= 112.5 and degree < 157.5:
        return "south east"
    
    # south
    elif degree >= 157.5 and degree < 202.5:
        return "south"
    # south west
    elif degree >= 202.5 and degree < 247.5:
        return "south west"
    
    # west
    elif degree >= 247.5 and degree < 292.5:
        return "west"
    # north west
    elif degree >= 292.5 and degree < 337.5:
        return "north west"
    
# categorize visibility
def get_visibility_options(visibility) -> float:
    """
    Parameters:
        visibility: float value to be coverted to kilometers
    returns:
        category of visibility
    """
    if (visibility / 1000) >= 10: # 10 kilometers
        return "excelent"
    if (visibility / 1000) >= 5: # 5 kilometers
        return "moderate"
    else:
        return "poor"

# connect and send email
def connect_email(sender_email, passCode, message) -> "str, str, str":
    """
    Parameters:
        sender_email: Email address that python will use to send the email
        passCode: Sender App password from email provider. (NOT your current email password)
        message: message to be sent to the frovided recepient

    returns:
        This function creates a basic email with a subject and message and sends it using the SMTP server specified. 
    """
    # Set up email details
    receiver_email = "migashanevictoire@gmail.com"
    subject = "Your Morning Weather Forcast From Python"
    message = email_message

    # Create a multipart message object and set the headers
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    # Attach the message to the email
    msg.attach(MIMEText(message, 'plain'))

    # Set up the SMTP server and send the email
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Set up the SMTP server and send the email:
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, passCode)
        server.send_message(msg)
        # server.sendmail(sender_email, receiver_email,msg)
        print("Email sent successfuly!")

    except Exception as e:
        print(f"Error sending email: {e}")
    finally:
        server.quit()