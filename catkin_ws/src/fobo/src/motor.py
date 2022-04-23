import RPi.GPIO as GPIO


class Motor():
    '''
        Constructor function
        @params: 
            pinA (int): pin number for direction 1 "IN1"
            pinB (int): pin number for direction 2 "IN2"
            en (int): pin number for speed motor, EN
        @return: None
    '''
    def __init__(self, pinA, pinB, en):
        self.pinA = pinA
        self.pinB = pinB
        self.speed = 50
        # Set up output pins
        GPIO.setup(self.pinA, GPIO.OUT)
        GPIO.setup(self.pinB, GPIO.OUT)
        GPIO.setup(en, GPIO.OUT)
        # Set up pwm output
        self.p = p=GPIO.PWM(en,1000)
        self.p.start(self.speed)


    '''
    Table to set up direction motor
                FORWARD BACKWARD    STOP
        pinA    HIGH    LOW         LOW
        pinB    LOW     HIGH        LOW
    '''


    '''
        set up motor in forward sense according to table
        @params: None
        @return: None
    '''
    def forward(self):
        GPIO.output(self.pinA, GPIO.HIGH)
        GPIO.output(self.pinB, GPIO.LOW)

    '''
        set up motor in backward sense according to table
        @params: None
        @return: None
    '''
    def backward(self):
        GPIO.output(self.pinA, GPIO.LOW)
        GPIO.output(self.pinB, GPIO.HIGH)

    '''
        stop motors according to table
        @params: None
        @return: None
    '''
    def stop(self):
        GPIO.output(self.pinA, GPIO.LOW)
        GPIO.output(self.pinB, GPIO.LOW)

    '''
        Change motor speed byt changing Duty Cycle in pwm output
        @params:
            speed (int 0-100): DT meaning speed
        @return: None
    '''
    def change_speed(self, speed):
        if speed > 100:
            self.speed = 100
        elif speed < 0:
            self.speed = 0
        else:
            self.speed = speed
        self.p.ChangeDutyCycle(self.speed)

def main():
    GPIO.setmode(GPIO.BOARD)
    motorR = Motor(pinA = 11, pinB = 15, en = 13)
    motorL = Motor(pinA = 10, pinB = 8, en = 12)
    
    while(1):
        act = input()

        if act == 'f':
            motorR.forward()
            motorL.forward()
        elif act == 'b':
            motorR.backward()
            motorL.backward()
        elif act == 's':
            motorR.stop()
            motorL.stop()
        elif act == 'h':
            motorR.change_speed(100)
            motorL.change_speed(100)
        elif act == 'm':
            motorR.change_speed(75)
            motorL.change_speed(75)
        elif act == 'r':
            print(f'speed {motorR.speed-25}')
            motorR.change_speed(motorR.speed-25)
            motorL.change_speed(motorR.speed-25)
        elif act == 'a':
            print(f'speed {motorR.speed+25}')
            motorR.change_speed(motorR.speed+25)
            motorL.change_speed(motorR.speed+25)
        elif act == 'e':
            motorR.stop()
            motorL.stop()
            GPIO.cleanup()
            break


if __name__ == '__main__':
    main()