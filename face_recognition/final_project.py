from multiprocessing import Process
from servo import servo
from rfid import read
from switch import switch
import RPi.GPIO as GPIO
import face_recog as FR
import cv2
import os
import time

def open_door():
    GPIO.output(gpio_led, GPIO.HIGH)
    servo.servoMoter(gpio_servo, 5)
    GPIO.output(gpio_led, GPIO.LOW)
    
def add_account():
    print("reading rfid...")
    if read.addID():
        print("add account process end")

def process_rfid():
    print("rfid process running")
    while True:
        if read.rfid():
            open_door()
            
            #manager mode
            if switch.switch(gpio_sw):
                print("access manager mode")
                time.sleep(2)
                
                add_account()
                
                print("access manager mode end")
                

if __name__ == '__main__':
    gpio_servo = 16
    gpio_led = 40
    gpio_sw = 37
    
    before_member = "unknown"
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(gpio_led,GPIO.OUT)
    GPIO.setup(37, GPIO.IN)
    GPIO.output(gpio_led, GPIO.LOW)
    
    #rfid process
    proc = Process(target=process_rfid, args=())
    proc.start()
    
    #parent process
    print("parent process running")
    face_recog = FR.FaceRecog()
    print(face_recog.known_face_names)
    while True:
        try:
            frame, is_known = face_recog.get_frame()
            
            # show the frame
            #cv2.imshow("Frame", frame)
            #key = cv2.waitKey(1) & 0xFF
            
            #open door
            if is_known != "unknown" and before_member != is_known:
                before_member = is_known
                print(is_known)
                open_door()

            # if the `q` key was pressed, break from the loop
            #if key == ord("q"):
                #proc.terminate()
                #break
        
        except KeyboardInterrupt:
            proc.terminate()
            break
        

    # do a bit of cleanup
    #cv2.destroyAllWindows()
    print('finish')