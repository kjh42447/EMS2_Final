#https://www.instructables.com/How-to-Interface-RFID-RC522-With-Raspberry-Pi/
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)
reader = SimpleMFRC522()

#read id list
f = open("./rfid/id_list.txt", 'r')
id_list = f.readlines()
f.close()

for i in range(len(id_list)):
    id_list[i] = int(id_list[i][:-1])

def addID():
    try:
        id, text = reader.read()
        print(id)
        print(type(id))
        print(text)
        sleep(1)
        
        if id in id_list:
            print("This ID is already in use")
            return False
        else:
            id_list.append(id)
            f = open("./rfid/id_list.txt", 'a')
            data = "%d\n" % id
            f.write(data)
            print("%d is appended"%id)
            f.close()
            return True
        
    except:
            GPIO.cleanup()
            

def rfid():
    try:
        id, text = reader.read()
        print(id)
        print(type(id))
        print(text)
        sleep(1)
        
        if id in id_list:
            return True
        else:
            return False
    except:
            GPIO.cleanup()
