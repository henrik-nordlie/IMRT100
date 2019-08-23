import RPi.GPIO as GPIO
import time

LED_PIN = 2
BUTTON_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)



led_on = False
GPIO.setup(LED_PIN, led_on)

prev_button_pressed = GPIO.input(BUTTON_PIN)


while True:
    current_button_pressed = GPIO.input(BUTTON_PIN)

    if current_button_pressed and not prev_button_pressed:
        led_on = not led_on
        GPIO.output(LED_PIN, led_on)
        print("LED on:", led_on)

    prev_button_pressed = current_button_pressed
    time.sleep(0.05)
