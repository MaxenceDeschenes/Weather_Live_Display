import serial
import requests
import time

# Set up the COM7 port for UART communication with FPGAot
ser = serial.Serial('COM7', 9600, timeout=1) 

# Geocoding API to get lat/lon from city name
GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

def get_coordinates(city):
    try:
        params = {'name': city, 'count': 1}
        response = requests.get(GEOCODE_URL, params)
        data = response.json()
        results = data.get("results")
        if results:
            lat = results[0]['latitude']
            lon = results[0]['longitude']
            return lat, lon
        else:
            print(f"No coordinates found for {city}.")
            return None, None
    except Exception as e:
        print(f"Error getting coordinates: {e}")
        return None, None

def get_weather_data(lat, lon):
    try:
        params = {
            'latitude': lat,
            'longitude': lon,
            'current_weather': 'true',
            'temperature_unit': 'celsius',
        }
        response = requests.get(WEATHER_URL, params)
        return response.json()
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

def format_weather_data(data):
    try:
        temp = int(data['current_weather']['temperature'])
        temp_str = f"{temp:06d}"
        ser.write(temp_str.encode())
        print(f"Sent temperature {temp_str} to FPGA")
    except Exception as e:
        print(f"Error formatting/sending data: {e}")

def main():
    city = input("Enter the city: ")
    lat, lon = get_coordinates(city)
    if lat is None or lon is None:
        return

    while True:
        data = get_weather_data(lat, lon)
        if data:
            format_weather_data(data)
        time.sleep(600)  # 10 minute refresh

if __name__ == '__main__':
    main()
