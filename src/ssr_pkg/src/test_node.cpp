#include "ros/ros.h"
#include "std_msgs/String.h"

int main(int argc, char  *argv[])
{
    ros::init(argc,argv,"test_node");
    printf("小园香径独徘徊\n");
    ros::NodeHandle nh;
    ros::Publisher pub = nh.advertise<std_msgs::String>("test_MSGS",10);
    ros::Rate loop_rate(10);
    while(ros::ok())
    {
        printf("可叹落叶飘零\n");
        std_msgs::String msg;
        msg.data = "Aniya";
        pub.publish(msg);
        loop_rate.sleep();

    }
    return 0;
}
