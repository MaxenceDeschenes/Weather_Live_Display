import serial
import requests
import time

# Set up the COM7 port for UART communication with FPGA
ser = serial.Serial('COM7', 9600, timeout=1)  # Added timeout for reliability

# Open-Meteo API endpoint for current weather
BASE_URL = "https://api.open-meteo.com/v1/forecast"

# Fetch weather data for Ottawa
def get_weather_data():
    try:
        params = {
            'latitude': 45.4215,  # Latitude of Ottawa
            'longitude': -75.6972,  # Longitude of Ottawa
            'current_weather': 'true',  # Only get current weather
            'temperature_unit': 'celsius',  # Temperature in Celsius
        }
        response = requests.get(BASE_URL, params=params)
        return response.json()
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

# Format the weather data to display on 7-segment display
def format_weather_data(data):
        # Get the current temperature from the API response
        temp = int(data['current_weather']['temperature'])
    
        temp_str = f"{temp:06d}"
        
        # Send the entire string at once
        ser.write(temp_str.encode())
        
        print(f"Sent temperature {temp_str} to FPGA")


def main():
    while True:
            data = get_weather_data()
            if data:
                format_weather_data(data)
            # Wait for 10 minutes before next update
            time.sleep(600)


if __name__ == '__main__':
    main()