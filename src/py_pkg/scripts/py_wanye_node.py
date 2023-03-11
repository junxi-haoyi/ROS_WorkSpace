#!/usr/bin/env python3
#coding=utf-8

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node("py_wanye_node")
    rospy.logwarn("云隐，夜明!")

    pub = rospy.Publisher("py_wangye",String,queue_size=10)

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rospy.loginfo("可叹落叶飘零~")
        msg = String()
        msg.data = "万叶"
        pub.publish(msg)
        rate.sleep()