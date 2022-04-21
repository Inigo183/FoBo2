import RPi.GPIO as GPIO


class Motor():
    def __init__(self, pinA, pinB, en):
        self.pinA = pinA
        self.pinB = pinB
        self.speed = 50

        GPIO.setup(self.pinA, GPIO.OUT)
        GPIO.setup(self.pinB, GPIO.OUT)
        GPIO.setup(en, GPIO.OUT)
        self.p = p=GPIO.PWM(en,1000)
        self.p.start(self.speed)
        
        self.valueA = GPIO.LOW
        self.valueA = GPIO.LOW


    def forward(self):
        GPIO.output(self.pinA, GPIO.HIGH)
        GPIO.output(self.pinB, GPIO.LOW)

    def backward(self):
        GPIO.output(self.pinA, GPIO.LOW)
        GPIO.output(self.pinB, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.pinA, GPIO.LOW)
        GPIO.output(self.pinB, GPIO.LOW)

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