import time
import board
import adafruit_sht31d

print("Raspberry Pi Freezer Monitor")

# Initialize I2C connection
i2c = board.I2C()

# Initialize SHT31 sensor
sensor = adafruit_sht31d.SHT31D(i2c)

print("SHT31 sensor initialized.")

while True:
    # Read freezer temperature
    temperature = sensor.temperature

    # Display temperature in the terminal
    print(f"Freezer temperature: {temperature:.1f} C")

    # Wait one second before the next measurement
    time.sleep(1)