import RPi.GPIO as GPIO
import time

def servoMoter(pin, t):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    pwm = GPIO.PWM(pin, 50)
    
    pwm.start(3)
    time.sleep(0.3)
    
    GPIO.setup(pin, GPIO.IN)
    time.sleep(t)
    
    GPIO.setup(pin, GPIO.OUT)
    pwm.ChangeDutyCycle(12)
    time.sleep(1)
    
    pwm.stop()
    GPIO.cleanup(pin)
    