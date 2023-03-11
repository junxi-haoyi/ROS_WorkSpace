#!/usr/bin/env python3
#coding=utf-8

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node("py_ying_node")
    rospy.logwarn("此刻，寂灭之时！")

    pub = rospy.Publisher("py_ying",String,queue_size=10)

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rospy.loginfo("稻光，亦是永恒！")
        msg = String()
        msg.data = "影"
        pub.publish(msg)
        rate.sleep()