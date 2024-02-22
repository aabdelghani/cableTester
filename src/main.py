import time
import RPi.GPIO as GPIO
import json 

# Function to load GPIO pin configurations from a JSON file
def load_config(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Load the pin configurations
config = load_config('../config/gpio_config.json')

# Assign pins from the loaded configuration
OutPins = config["OutPins"]
InPinsA = config["InPinsA"]
InPinsB = config["InPinsB"]
Indicator = config["Indicator"]

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(Indicator, GPIO.OUT)
GPIO.output(Indicator, GPIO.LOW)

# Setup the pins as outputs or inputs with pull-up resistors
for pin in OutPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

for pin in InPinsA + InPinsB:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize connection status list
ConnStatus = [0] * len(OutPins)

# Function to check if all connections are correct
def verifyLinks(ConnStatus):
    for status in ConnStatus:
        if status != 1:
            return False  # If any status is not 1, return False
    return True  # If all statuses are 1, return True

# Main execution loop
try:
    while True:
        # Check each pair of pins for their connection status
        for i, out_pin in enumerate(OutPins):
            in_pin_a = InPinsA[i % len(InPinsA)]
            in_pin_b = InPinsB[i % len(InPinsB)]  
            # Check if both corresponding input pins are LOW (connected)
            if GPIO.input(in_pin_a) == 0 and GPIO.input(in_pin_b) == 0:
                ConnStatus[i] = 1  # Connection is correct
                print(f"Pin {out_pin} to Pins {in_pin_a} & {in_pin_b}: CONNECTED")
            else:
                ConnStatus[i] = 0  # Connection is incorrect
                print(f"Pin {out_pin} to Pins {in_pin_a} & {in_pin_b}: DISCONNECTED")
        
        # Update the LED based on the overall connection status
        if verifyLinks(ConnStatus):
            GPIO.output(Indicator, GPIO.HIGH)  # Turn on LED if all connections are correct
        else:
            GPIO.output(Indicator, GPIO.LOW)  # Turn off LED if any connection is incorrect
        
        time.sleep(1)  # Pause before the next check

except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO settings on exit
