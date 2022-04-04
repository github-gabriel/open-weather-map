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

place = input("Place: ")

try:
    observation = mgr.weather_at_place(place)
    w = observation.weather
    def time_difference():
        geolocator = Nominatim(user_agent="geoapiExercises")

        print("Location address: ", place)

        location = geolocator.geocode(place)

        print("Latitude and Longitude: ")
        print((location.latitude, location.longitude))

        obj = TimezoneFinder()

        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        print("Time Zone: ", result)

        timezone = pytz.timezone(result)
        date = datetime.now(timezone)
        return date

    def get_temperature():
        tmp = w.temperature('celsius')
        return tmp['temp']

    def get_sunrise():
        sunrise = w.to_dict()
        return sunrise['sunrise_time']

    def get_sunset():
        sunset = w.to_dict()
        return sunset['sunset_time']

    def get_wind_speed():
        wind_speed = w.wind('meters_sec')
        return wind_speed['speed']


    def get_humidity():
        humidity = w.to_dict()
        return humidity['humidity']

    def get_pressure():
        pressure = w.to_dict()
        return pressure['press']

    def get_reference_time():
        reference_time = w.to_dict()
        return reference_time['reference_time']

    def get_clouds():
        clouds = w.to_dict()
        return clouds['clouds']

    def get_status():
        status = w.to_dict()
        return status['detailed_status']

    def get_pressure():
        pressure = w.to_dict()
        pressure = pressure['pressure']
        return pressure['press']

    def get_temperature_1():
        feels_like = w.temperature('celsius')
        return feels_like['feels_like']

    sunrise_time = get_sunrise()
    sunset_time = get_sunset()
    Wind_speed = get_wind_speed()
    Wind_speed = Wind_speed * 3600
    Wind_speed = Wind_speed / 1000
    Reference_time = get_reference_time()

    time_of_place = time_difference().replace(microsecond=0)
    offset = time_of_place.utcoffset().total_seconds() / 60  # Offset in Seconds / 60 -> Minutes
    print('UTC Offset [Min]: {}'.format(offset))  # Offset in Minutes

    minutes = offset  # Offset in Minutes

    sunset = datetime.utcfromtimestamp(sunset_time) + timedelta(minutes=minutes)  # Sunset-Time + UTC Offset
    sunset = sunset.strftime('%d-%m-%Y %H:%M:%S')

    sunrise = datetime.utcfromtimestamp(sunrise_time) + timedelta(minutes=minutes)  # Sunrise-Time + UTC Offset
    sunrise = sunrise.strftime('%d-%m-%Y %H:%M:%S')

    reference = datetime.utcfromtimestamp(Reference_time) + timedelta(minutes=minutes)  # Reference Time + UTC Offset
    reference = reference.strftime('%d-%m-%Y %H:%M:%S')

    print("Temperature [Celsius]: ", get_temperature(), "/ Feels like [Celsius]:", get_temperature_1())  # Temperatur
    print("Sunrise: ", sunrise)  # Sonnenaufgang Uhrzeit
    print("Sunset: ", sunset)  # Sonnenuntergang Uhrzeit
    print("Reference Time [Current time in the country]: ", reference)  # Referenzzeit
    print("Wind speed: ", round(Wind_speed), "km/h")  # Windgeschwindigkeit
    print("Humidity: ", get_humidity())  # Luftfeuchtigkeit
    print("Status: ", get_status())  # Genereller Status
    print("Cloud cover: ", get_clouds(), "%")  # Wolkenbedeckung
    print("Pressure: ", get_pressure())  # Druck

    input()

except:
    print("A error occurred!")

    input()