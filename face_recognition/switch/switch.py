import RPi.GPIO as GPIO
import time

def switch(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.IN)
    
    sw_value = GPIO.input(pin)
    
    GPIO.cleanup(pin)
    
    return sw_value