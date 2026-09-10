import time
import board
import adafruit_sht31d
import RPi.GPIO as GPIO

print("Raspberry Pi Freezer Monitor")

# GPIO pin numbers
GREEN_LED = 17
YELLOW_LED = 27
RED_LED = 22

UP_BUTTON = 23
DOWN_BUTTON = 24

# Temperature settings
WARNING_TEMPERATURE = -10.0
critical_limit = -3.0

# Configure GPIO numbering
GPIO.setmode(GPIO.BCM)

# Configure LEDs
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(YELLOW_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

# Configure buttons with internal pull-up resistors
GPIO.setup(UP_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(DOWN_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize I2C connection
i2c = board.I2C()

# Initialize SHT31 sensor
sensor = adafruit_sht31d.SHT31D(i2c)

print("SHT31 sensor initialized.")
print(f"Critical temperature limit: {critical_limit:.1f} C")

try:
    while True:
        # Read buttons
        if GPIO.input(UP_BUTTON) == GPIO.LOW:
            critical_limit += 1.0

            print(
                f"Critical limit increased to "
                f"{critical_limit:.1f} C"
            )

            time.sleep(0.3)

        if GPIO.input(DOWN_BUTTON) == GPIO.LOW:
            critical_limit -= 1.0

            print(
                f"Critical limit decreased to "
                f"{critical_limit:.1f} C"
            )

            time.sleep(0.3)

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
        elif temperature < critical_limit:
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
        print(f"Critical limit: {critical_limit:.1f} C")
        print("------------------------")

        time.sleep(1)

except KeyboardInterrupt:
    print("Program stopped.")

finally:
    GPIO.cleanup()