import RPi.GPIO as GPIO
import time
import signal
import sys
import numpy as np
import matplotlib.pyplot as plt


# use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
#pinTrigger = 14
#pinEcho = 15


def mes(pinTrigger,pinEcho,num,pos):
    def close(signal, frame):
        print("\nTurning off ultrasonic distance detection...\n")
        GPIO.cleanup() 
        sys.exit(0)
    signal.signal(signal.SIGINT, close)

    # set GPIO input and output channels
    GPIO.setup(pinTrigger, GPIO.OUT)
    GPIO.setup(pinEcho, GPIO.IN)

    while True:
        # set Trigger to HIGH
        GPIO.output(pinTrigger, True)
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(pinTrigger, False)

        startTime = time.time()
        stopTime = time.time()

        # save start time
        while 0 == GPIO.input(pinEcho):
            startTime = time.time()

        # save time of arrival
        while 1 == GPIO.input(pinEcho):
            stopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = stopTime - startTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
        x=pos
        y = distance
        # plt.scatter(x,y)

        print ("Distance "+ num +": %.1f cm" % distance)
        time.sleep(1)
        break
        
#plt.show()
while True:
    
    
    mes(4,17,"FL",4) # good
    mes(27,22,"FLC",3) # good
    mes(10,9,"FRC",2) # good
    mes(11,0,"FR",1) # good (front right plugged in)

    # mes(2,3,"RR",4) # bad (rear right plugged in)
    # mes(5,6,"RRC",3) # bad
    # mes(13,19,"RLC",2) #bad
    # mes(26,20,"RL",1) # good
    # plt.show()
    # plt.draw()
