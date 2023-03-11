#!/usr/bin/env python3
#coding=UTF-8

#import pkg from pip
import rospy
from std_msgs.msg import String
import serial as ser
import Jetson.GPIO
import time
#import pkg 

#callback function
def wanye_CallBack(msg):
    rospy.loginfo(msg.data)
    time.sleep(1)
    se.write(a.encode())
    print("send Aniya")
    time.sleep(1)
    se.write(b.encode())
    print("send SPY")
    print(msg.data)



def ying_CallBack(msg):
    rospy.loginfo(msg.data)
    print(msg.data)
    time.sleep(1)


#callback



#initialization USART and param
a="Aniya\n"
b="SPY\n"
se = ser.Serial("/dev/ttyTHS1",9600,timeout=1)

rospy.init_node("USART_node")
rospy.logwarn("USART_NODE_init")
sub = rospy.Subscriber("py_wangye",String,wanye_CallBack,queue_size=10)
sub = rospy.Subscriber("py_ying",String,ying_CallBack,queue_size=10)
#initialization


if __name__ == '__main__':
    rospy.spin()

        
