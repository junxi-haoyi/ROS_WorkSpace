#include "ros/ros.h"
#include "std_msgs/String.h"

void SPY_receive(std_msgs::String msg)
{
    ROS_INFO(msg.data.c_str());//receiving the  time function will printf time of receiving

}

void test_receive(std_msgs::String msg)
{
    ROS_INFO(msg.data.c_str());//receiving the  time function will printf time of receiving

}



int main(int argc, char  *argv[])
{
    ros::init(argc,argv,"sbcb_node");
    ros::NodeHandle nh;
    ros::Subscriber sub_1 = nh.subscribe("SPY_MSGS",10,SPY_receive);
    ros::Subscriber sub_2 = nh.subscribe("test_MSGS",10,test_receive);
    while(ros::ok())
    {
        ros::spinOnce();//check to see if the msgs arrives
    }
    return 0;
}
