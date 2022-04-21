#!/usr/bin/env python3
import sys
import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty
from fobo.msg import Direction

msg = """
Reading from the keyboard  and Publishing to Twist!
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

For Holonomic mode (strafing), hold down the shift key:
---------------------------
   U    I    O
   J    K    L
   M    <    >

t : up (+z)
b : down (-z)

anything else : stop

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%

CTRL-C to quit
"""
moveBindings = {
        'w': (1, 0),
        's': (-1, 0),
        'd': (0, 1),
        'a': (0, -1),
        'q': (1, -1),
        'e': (1, 1),
        'p': (0, 0),
           }

speedBindings={
        'i': (10, 0),
        'k': (-10,0),
        'j': (0, -10),
        'l': (0, 10),
          }

def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

speed = 50
turn = 50

def vels(speed,turn):
    return "currently:\tspeed %s\tturn %s " % (speed,turn)


def limits(n):
    if n > 100:
        return 100
    elif n < -100:
        return -100
    else:
        return n


if __name__ == '__main__':
    settings = termios.tcgetattr(sys.stdin) 

    pub = rospy.Publisher('/direction', Direction, queue_size = 1)
    rospy.init_node('moving')
    
    x = 0
    z = 0
    status = 0
    
    try:
        print(msg)
        print(vels(speed,turn))
        while(1):
            key = getKey()
            if key in moveBindings.keys():
                x = moveBindings[key][0]
                z = moveBindings[key][1]
            elif key in speedBindings.keys():
                speed = limits(speed + speedBindings[key][0])
                turn = limits(turn + speedBindings[key][1])
    
                print(vels(speed,turn))
                if (status == 14):
                    print(msg)
                status = (status + 1) % 15
            else:
                x = 0
                z = 0
                if (key == '\x03'):
                    break
    
            dir = Direction()
            dir.x = x*speed
            dir.z = z*turn
            pub.publish(dir)
    
    except:
        print('e')
    
    finally:
        dir = Direction()
        dir.x = 0
        dir.z = 0
        pub.publish(dir)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

    
        