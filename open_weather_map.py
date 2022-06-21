from pyowm import OWM

from datetime import timedelta
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz

owm = OWM('YOUR_OPEN_WEATHER_MAP_API_KEY')
mgr = owm.weather_manager()

print(""" 
██╗    ██╗███████╗ █████╗ ████████╗██╗  ██╗███████╗██████╗  
██║    ██║██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗  
██║ █╗ ██║█████╗  ███████║   ██║   ███████║█████╗  ██████╔╝    
██║███╗██║██╔══╝  ██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗    
╚███╔███╔╝███████╗██║  ██║   ██║   ██║  ██║███████╗██║  ██║     
 ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝""")

place = input("Ort: ")

observation = mgr.weather_at_place(place)
w = observation.weather


def time_difference():
    geolocator = Nominatim(user_agent="geoapiExercises")

    print("\nOrt: ", place)

    location = geolocator.geocode(place)

    print("Breiten- und Längengrad: ", location.latitude, location.longitude)

    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    print("Zeitzone: ", result)

    timezone = pytz.timezone(result)
    date = datetime.now(timezone)
    return date


def get_temp():
    temp = w.temperature('celsius')
    return temp['temp']


def get_speed():
    speed = w.wind('meters_sec')
    return speed['speed']


def get_pressure():
    pressure = w.to_dict()
    pressure = pressure['pressure']
    return pressure['press']


def get_feels_like():
    feels_like = w.temperature('celsius')
    return feels_like['feels_like']


sunrise_time = w.to_dict()['sunrise_time']
sunset_time = w.to_dict()['sunset_time']
Wind_speed = get_speed()
Wind_speed = Wind_speed * 3600
Wind_speed = Wind_speed / 1000
Reference_time = w.to_dict()['reference_time']

time_of_place = time_difference().replace(microsecond=0)
offset = time_of_place.utcoffset().total_seconds() / 60  # Offset in Seconds / 60 -> Minutes
print('UTC Offset [Min]: {}'.format(offset) + "\n")  # Offset in Minutes

minutes = offset  # Offset in Minutes

sunset = datetime.utcfromtimestamp(sunset_time) + timedelta(minutes=minutes)  # Sunset-Time + UTC Offset
sunset = sunset.strftime('%d-%m-%Y %H:%M:%S')

sunrise = datetime.utcfromtimestamp(sunrise_time) + timedelta(minutes=minutes)  # Sunrise-Time + UTC Offset
sunrise = sunrise.strftime('%d-%m-%Y %H:%M:%S')

reference = datetime.utcfromtimestamp(Reference_time) + timedelta(minutes=minutes)  # Reference Time + UTC Offset
reference = reference.strftime('%d-%m-%Y %H:%M:%S')

print("Temperatur [Celsius]: ", get_temp(), "/ Gefühlt [Celsius]:", get_feels_like())  # Temperatur
print("Sonnenaufgang: ", sunrise)  # Sonnenaufgang Uhrzeit
print("Sonnenuntergang: ", sunset)  # Sonnenuntergang Uhrzeit
print("Referenz-Zeit [Aktuelle Zeit in " + place + "]: ", reference)  # Referenzzeit
print("Windgeschwindigkeit: ", round(Wind_speed), "km/h")  # Windgeschwindigkeit
print("Luftfeuchtigkeit: ", w.to_dict()['humidity'], "%")  # Luftfeuchtigkeit
print("Status: ", w.to_dict()['detailed_status'])  # Genereller Status
print("Wolkenbedeckung: ", w.to_dict()['clouds'], "%")  # Wolkenbedeckung
print("Druck: ", get_pressure())  # Druck

input()
