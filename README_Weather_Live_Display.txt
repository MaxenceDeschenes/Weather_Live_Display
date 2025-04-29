🌦️ Weather Live Display to FPGA
Overview
This project implements a real-time temperature display system on an FPGA using UART communication. A Python script fetches weather data from the Open-Meteo API and transmits it to the FPGA, which processes and displays the temperature on a 6-digit 7-segment display. The system now supports user-input for selecting the city, allowing it to fetch the weather data based on the user's location.

How It Works
The system works in the following steps:

The user is prompted to input their city.

The Python script uses the Open-Meteo Geocoding API to convert the city name into latitude and longitude coordinates.

The coordinates are used to fetch current weather data from the Open-Meteo Weather API.

The temperature is extracted from the weather data and formatted for transmission.

The formatted temperature is sent to the FPGA via UART, where it is displayed on a 6-digit 7-segment display.

The system refreshes every 10 minutes, updating the temperature on the FPGA display.

New Features:
City-based weather retrieval: Users can now input any city name to fetch weather data specific to their location.

Error handling: If the city is not found or the weather data is unavailable, the script handles errors gracefully, ensuring a smooth experience.

Real-time updates: The system continuously fetches weather data and updates the FPGA display every 10 minutes.

Modules and Components
UART Receiver
Captures temperature data at 9600 baud.

Converts ASCII values into binary digits.

Stores received values for display updates.

7-Segment Display Driver
Uses predefined 7-bit encoding for digits 0-9.

Refreshes display at 200Hz using multiplexing.

Cycles through 6 digits for continuous updates.

Debugging
A blinking LED confirms the clock is functioning correctly.

Next Steps
Multi-city support: Implement functionality to fetch weather data for multiple cities and cycle through them on the FPGA display.

Support for negative temperatures: Modify the FPGA display to correctly handle and show negative temperatures.

UART transmission efficiency: Improve the efficiency of UART transmission, reducing delays and optimizing data flow.

Requirements
FPGA development board (Cyclone 4 E or similar)

Python 3 with the requests and pyserial libraries

Open-Meteo API access (no authentication required)

6-digit 7-segment display

UART communication module

Installation
Set up FPGA:

Load the Verilog code into your FPGA development environment (Quartus or other).

Compile and upload the design to the FPGA.

Connect the 6-digit 7-segment display and UART module to the appropriate FPGA pins.

Set up Python Environment:

Install the necessary Python packages:

pip install requests pyserial
Run the Python script to fetch weather data and transmit it to the FPGA:

python weather_live_display.py
Observe the Display:

The temperature will be updated on the 7-segment display on the FPGA every 10 minutes based on the city you input.

Pin Planner
The pin planner is configured specifically for the Cyclone 4 E FPGA family. Adjustments may be needed for other FPGA models. Refer to the documentation for your specific FPGA board for pin mapping.
