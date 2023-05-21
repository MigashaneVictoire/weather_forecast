import requests
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
    celsius = kelvin - 273.15
    return round(celsius, 2)

# categorize compass
def compass(degree):
    # north
    if degree >= 337.5 or degree in np.arange(0.0,22.5, 0.1):
        return "north"
    #north east
    elif degree in np.arange(22.5, 67.5, 0.1):
        return "north east"
    
    # east
    elif degree in np.arange(67.5, 112.5, 0.1):
        return "east"
    # south east
    elif degree in np.arange(112.5, 157.5, 0.1):
        return "south east"
    
    # south
    elif degree in np.arange(157.5, 202.5, 0.1):
        return "south"
    # south west
    elif degree in np.arange(202.5, 247.5, 0.1):
        return "south west"
    
    # west
    elif degree in np.arange(247.5, 292.5, 0.1):
        return "west"
    # north west
    elif degree in np.arange(292.5, 337.5, 0.1):
        return "north west"
    
# categorize visibility
def get_visibility_options(visibility) -> float:
    """
    
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