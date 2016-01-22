import RPi.GPIO as GPIO
import time

GPIO.cleanup()


GPIO.setmode(GPIO.BCM)
GPIO.setup(9,GPIO.IN)

while True:
        input_value = GPIO.input(9)
        if input_value == 0:
                print(GPIO.input(9))
        else:
                print("the motion is detected")
        
	time.sleep(0.5)
