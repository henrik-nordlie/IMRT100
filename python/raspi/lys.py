import RPi.GPIO as GPIO
import time

LED_PIN = 2

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT)

while True:
    GPIO.output(LED_PIN, True)
    print("LED on")
    time.sleep(0.4)

    GPIO.output(LED_PIN, False)
    print("LED off")
    time.sleep(0.4)
