#!/usr/bin/env python3
import rospy
import RPi.GPIO as GPIO
from motor import Motor
from fobo.msg import Direction

'''
class to vehicle direction and speed control

'''
class Direction_vehicle():
    '''
    constructor function
    @params:
        pinLA (int): pin number for lef motor, IN1
        pinLB (int): pin number for lef motor, IN2
        enL (int): pin number for lef motor speed, ENA
        pinRA (int): pin number for right motor, IN3
        pinLB (int): pin number for right motor, IN4
        enL (int): pin number for right motor speed, ENB
    '''
    def __init__ (self, pinLA, pinLB, enL, pinRA, pinRB, enR):
        # Set up GPIO
        GPIO.setmode(GPIO.BOARD)
        # Create object for each motor with their corresponding pins
        self.motorL = Motor(pinA = pinLA, pinB = pinLB, en = enL)
        self.motorR = Motor(pinA = pinRA, pinB = pinRB, en = enR)
        # Machine status initialized as stop
        self.status = 'stop'
        self.forward = False
        self.speed = 0
        self.turning = 0

    '''
        Function called when message is recived
        @param:
            data (fobo/Direction): message recived
        @return: None
    '''
    def callback(self, data):
    # Set up motor in forward sense
        rospy.loginfo(data)
        # Now message is checked and compared if machine status has changed
        if data.x == 0 and data.z == 0 and self.status != 'stop':
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
            
        # Apply speed change if message speed is different 
        if abs(data.x) != self.speed:
            self.change_speed(abs(data.x))

        # If there is any turn, apply it
        if data.z != 0:
            self.turn(data.z)
        else:
            self.turning = 0


    '''
        Function to launch subsriber nodo to topic /direction
        @param: None
        @return: None
    '''
    def recibe_node(self):
        rospy.init_node('direction', anonymous=True)
        rospy.Subscriber('/direction', Direction, self.callback)
        rospy.spin()

    '''
        Set motors in forward move
        @param: None
        @return: None
    '''
    def forward_mv(self):
        rospy.loginfo('forward')
        self.motorL.forward()
        self.motorR.forward()

    '''
        Set motors in backward move
        @param: None
        @return: None
    '''
    def backward_mv(self):
        rospy.loginfo('backward')
        self.motorL.backward()
        self.motorR.backward()

    '''
        Stop both motors
        @param: None
        @return: None
    '''
    def stop(self):
        rospy.loginfo('stop')
        self.motorL.stop()
        self.motorR.stop()

    '''
        Set speed in both motors
        @param:
            speed (int 0 - 100): linear speed
        @return: None
    '''
    def change_speed(self, speed):
        # Check speeds is in limits
        if speed > 100:
            self.speed = 100
        elif speed < 0:
            self.speed = 0
        else:
            self.speed = speed
        self.motorL.change_speed(self.speed)
        self.motorR.change_speed(self.speed)

    '''
        Set speed in each motor to create turning move
        @param:
            z (int -100 - 100): turning speed
        @return: None
    '''
    def turn(self, z):
        if z == self.turning:
            return

        self.turning = z
        # Positive z is turn left, so more power to right motor
        if z > 0:
            motor1 = self.motorR
            motor2 = self.motorL
        # Negative z is turn right, so more power to left motor
        else:
            motor1 = self.motorL
            motor2 = self.motorR
        
        # Add turn speed to motor speed
        total_speed = abs(motor1.speed) + abs(z)

        # If motors are running in diferent speeds, add z speed to motor 2 
        # so motor 1 has z more speed tan motor 2
        if motor1.speed != motor2.speed:
            total_speed = abs(motor2.speed) + abs(z)

        # If speed calculated is less than 100, just apply it
        if total_speed <= 100:
            motor1.change_speed(total_speed)
            rospy.loginfo(f'motor1: {motor1.speed}')
            return

        # In other case, motor 1 at maximum speed and reduce motor 2
        motor1.change_speed(100)
        
        # (total_speed - 100) is the "overflow" of speed,
        # if motor2 speed minus overflow is positive, just apply that speed
        if motor2.speed - (total_speed - 100) > 0:
            motor2.change_speed(motor2.speed - (total_speed - 100))
            rospy.loginfo(f'motor2: {motor2.speed}')
            return

        # In other case, apply the speed in asbolute value and change turning sense
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