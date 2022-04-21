#!/usr/bin/env python3
import rospy
import RPi.GPIO as GPIO
from motor import Motor
from fobo.msg import Direction


class Direction_vehicle():
    def __init__ (self, pinLA, pinLB, enL, pinRA, pinRB, enR):
        GPIO.setmode(GPIO.BOARD)
        self.motorL = Motor(pinA = pinLA, pinB = pinLB, en = enL)
        self.motorR = Motor(pinA = pinRA, pinB = pinRB, en = enR)
        self.status = 'stop'
        self.forward = False
        # self.forward()
        self.speed = 0
        self.turning = 0

    def callback(self, data):
        rospy.loginfo(data)
        if data.x == 0 and data.z == 0:
            self.status = 'stop'
            self.stop()
            return

        if data.x > 0 and self.status != 'forward':
            self.forward = True
            self.status = 'forward'
            self.forward_mv()
        elif data.x < 0 and self.status != 'backward':
            self.forward = False
            self.status = 'backward'
            self.backward_mv()
            

        if abs(data.x) != self.speed:
            self.change_speed(abs(data.x))

        if data.z != 0:
            self.turn(data.z)
        else:
            self.turning = 0


    def recibe_node(self):
        rospy.init_node('direction', anonymous=True)
        rospy.Subscriber('/direction', Direction, self.callback)
        rospy.spin()

    def forward_mv(self):
        rospy.loginfo('forward')
        self.motorL.forward()
        self.motorR.forward()

    def backward_mv(self):
        rospy.loginfo('backward')
        self.motorL.backward()
        self.motorR.backward()

    def stop(self):
        rospy.loginfo('stop')
        self.motorL.stop()
        self.motorR.stop()

    def change_speed(self, speed):
        if speed > 100:
            self.speed = 100
        elif speed < 0:
            self.speed = 0
        else:
            self.speed = speed
        self.motorL.change_speed(self.speed)
        self.motorR.change_speed(self.speed)

    def turn(self, z):
        if z == self.turning:
            return

        self.turning = z

        if z > 0:
            motor1 = self.motorR
            motor2 = self.motorL
        else:
            motor1 = self.motorL
            motor2 = self.motorR

        total_speed = abs(motor1.speed) + abs(z)

        if motor1.speed != motor2.speed:
            total_speed = abs(motor2.speed) + abs(z)

        if total_speed <= 100:
            motor1.change_speed(total_speed)
            rospy.loginfo(f'motor1: {motor1.speed}')
            return

        motor1.change_speed(100)
        if motor2.speed - (total_speed - 100) > 0:
            motor2.change_speed(motor2.speed - (total_speed - 100))
            rospy.loginfo(f'motor2: {motor2.speed}')
            return

        motor2.change_speed(abs(motor2.speed - (total_speed - 100)))
        rospy.loginfo(f'motor2: {motor2.speed}')
        if self.forward:
            rospy.loginfo(f'motor2: forward')
            motor2.backward()
        else:
            rospy.loginfo(f'motor2: backward')
            motor2.forward()


if __name__ == '__main__':
    dir = Direction_vehicle(pinLA = 10, pinLB = 8, enL = 12,
                            pinRA = 11, pinRB = 15, enR = 13)
    dir. recibe_node()