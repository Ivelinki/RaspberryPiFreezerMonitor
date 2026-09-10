# Raspberry Pi Freezer Monitor

University project for monitoring freezer temperature with Raspberry Pi.

## Project Description

The system monitors the temperature inside a freezer using an SHT31 sensor.

The measured temperature is displayed on a 16x2 LCD display.

Three LEDs indicate the current freezer condition:

- Green LED - normal temperature
- Yellow LED - warning temperature
- Red LED - critical temperature

Two buttons are used to change the critical temperature limit.

The default critical temperature limit is:

-3 °C

## Hardware

- Raspberry Pi 4 Model B
- SHT31 temperature sensor
- LCD 16x2 with I2C module
- Green LED
- Yellow LED
- Red LED
- UP button
- DOWN button
- Resistors
- Breadboard
- Jumper wires

## GPIO Pins

- Green LED - GPIO17
- Yellow LED - GPIO27
- Red LED - GPIO22
- UP button - GPIO23
- DOWN button - GPIO24

## I2C Devices

SHT31 sensor:
- I2C connection
- Default address: 0x44

LCD 16x2:
- I2C connection
- Example address: 0x27

## Program Logic

The program continuously reads the freezer temperature.

The system has three states:

### NORMAL

Temperature is below -10 °C.

The green LED is turned on.

### WARNING

Temperature is between -10 °C and the critical limit.

The yellow LED is turned on.

### CRITICAL

Temperature is equal to or higher than the critical limit.

The red LED is turned on.

The default critical limit is -3 °C.

The UP and DOWN buttons can change this limit.

## Software

The project is written in Python.

Libraries used:

- Adafruit CircuitPython SHT31D
- Adafruit Blinka
- RPi.GPIO
- RPLCD
- smbus2

## Running the Program

The program is designed to run on Raspberry Pi OS with Python 3.

Main program:

```bash
python3 main.py