Weather Live Display

Overview

This project implements a real-time temperature display system on an FPGA using UART communication. A Python script fetches weather data from the Open-Meteo API and transmits it to the FPGA, which processes and displays the temperature on a 6-digit 7-segment display.

How It Works

The system receives temperature data via UART, decodes ASCII characters into binary digits, and updates the 7-segment display accordingly. The display refreshes at 200Hz for smooth updates, and a debug LED blinks to indicate system functionality.

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

Implement user input to allow selection of any city for weather retrieval.

Add support for displaying negative temperatures correctly.

Improve UART transmission efficiency and error handling.

Requirements

FPGA development board

Python 3 with requests and pyserial

Open-Meteo API access

Installation

Load the Verilog code into your FPGA development environment (e.g., Quartus).

Compile and upload the design to the FPGA.

Connect the 6-digit 7-segment display and UART module to the appropriate FPGA pins.

Run the Python script to fetch and transmit weather data.

Observe the temperature updates on the FPGA display.

Pin Planner

The pin planner is configured specifically for the Cyclone 4 E FPGA family. Adjustments may be needed for other FPGA models.