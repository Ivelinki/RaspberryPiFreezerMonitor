import time
import board
import adafruit_sht31d
import RPi.GPIO as GPIO

print("Raspberry Pi Freezer Monitor")

# GPIO pin numbers
GREEN_LED = 17
YELLOW_LED = 27
RED_LED = 22

# Temperature limits
WARNING_TEMPERATURE = -10.0
CRITICAL_TEMPERATURE = -3.0

# Configure GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(YELLOW_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

# Initialize I2C connection
i2c = board.I2C()

# Initialize SHT31 sensor
sensor = adafruit_sht31d.SHT31D(i2c)

print("SHT31 sensor initialized.")

try:
    while True:
        # Read freezer temperature
        temperature = sensor.temperature

        print(f"Freezer temperature: {temperature:.1f} C")

        # NORMAL
        if temperature < WARNING_TEMPERATURE:
            state = "NORMAL"

            GPIO.output(GREEN_LED, GPIO.HIGH)
            GPIO.output(YELLOW_LED, GPIO.LOW)
            GPIO.output(RED_LED, GPIO.LOW)

        # WARNING
        elif temperature < CRITICAL_TEMPERATURE:
            state = "WARNING"

            GPIO.output(GREEN_LED, GPIO.LOW)
            GPIO.output(YELLOW_LED, GPIO.HIGH)
            GPIO.output(RED_LED, GPIO.LOW)

        # CRITICAL
        else:
            state = "CRITICAL"

            GPIO.output(GREEN_LED, GPIO.LOW)
            GPIO.output(YELLOW_LED, GPIO.LOW)
            GPIO.output(RED_LED, GPIO.HIGH)

        print(f"Freezer state: {state}")
        print("------------------------")

        time.sleep(1)

except KeyboardInterrupt:
    print("Program stopped.")

finally:
    GPIO.cleanup()