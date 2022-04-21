#!/usr/bin/env python3
import rospy
import time
import RPi.GPIO as GPIO
from led.msg import led


def callback(data):
    if data.status:
        blink()


def blink():
    motor = 11
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(motor, GPIO.OUT)
    
    GPIO.output(motor, GPIO.HIGH)
    time.sleep(10)
    GPIO.output(motor, GPIO.LOW)
    GPIO.cleanup()



def recibe_node():
    msg = led()
    rospy.init_node('led', anonymous=True)
    rospy.Subscriber('/led', led, callback)
    rospy.spin()


if __name__ == '__main__':
    recibe_node()