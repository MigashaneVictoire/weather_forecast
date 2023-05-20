from pprint import pprint
import functions as func
import env

# send email importsi
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


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
is characterized by {description}. The temperature is {temp} Kelvin, with a maximum of {temp_max} Kelvin \
and a minimum of {temp_min} Kelvin. The humidity level is at {humidity}%, and the atmospheric pressure is {pressure} hPa.\
The wind is blowing at a speed of {speed} m/s from a direction of {degree} degrees. The visibility is \
--excellent-- at {visibility} meters. The weather condition is represented by the presence of {description}.\
The weather code is --804--, indicating the --cloudiness--. The sunrise occurred at --1684577705-- seconds \
since the Unix epoch, while the sunset is expected to happen at --1684631015-- seconds. {city} \
is located in the {country}, and the local time zone is --UTC-4 (Eastern Daylight Time)--."
    return email_message

# connect and send email
def connect_email(sender_email, passCode, message):

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
    smtp_server = "smtp.google.com"
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


# Program will run starting here
if __name__ == "__main__":
    # get cridentials
    api_key = env.open_weather_map_api_key()
    email, password = env.email_cridentials()

    print("~~~~~~ Welsome to 24 Weather Cast ~~~~~~")
    city_name = input("Enter a city name: ")
    city_name = city_name.replace(" ", "%20") # replace empty space if contained in city input
    
    # api request link
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    # data = func.full_curr_city_json(url)


    # user_preview = input("How would like your forcast? (Celsius 'C' or Fehrenheit 'F')\n")

    # All weather function call re-assignment
    lat, lon = func.get_coordinates(curr_data())
    temp, temp_min, temp_max = func.get_temperature(curr_data())
    feels_like, humidity, pressure= func.get_feels(curr_data())
    city, country = func.city_and_country_names(curr_data())
    description, icon = func.get_weather_description(curr_data())
    degree, speed = func.get_wind(curr_data())
    visibility = func.get_visibility(curr_data())

    # Full weather forecast message
    email_message = email_propt(lat, lon, 
                temp, temp_min, temp_max,
                feels_like, humidity, pressure,
                city, country,
                description, icon,
                degree, speed,
                visibility
                 )
    

    connect_email(email, password, email_message)