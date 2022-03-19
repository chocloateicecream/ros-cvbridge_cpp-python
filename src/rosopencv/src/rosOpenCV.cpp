#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <opencv2/highgui/highgui.hpp>
#include <cv_bridge/cv_bridge.h>
#include <stdio.h>

int main(int argc, char** argv)
{
    ros::init(argc, argv, "image_publisher");
    ros::NodeHandle nh;
    image_transport::ImageTransport it(nh);//用之前声明的节点
    //句柄初始化it，好像就是拿it代替了nh。
    cv::Mat image=cv::imread("/home/lee/lena.jpg");
    image_transport::Publisher pub=it.advertise("camera/image",1);
    if (image.empty())
    {
        printf("open error\n");
    }
    sensor_msgs::ImagePtr msg=cv_bridge::CvImage(std_msgs::Header(),"bgr8",image).toImageMsg();//图像格式转换
    sensor_msgs::Image msgpub;
    msgpub=*msg;
    ros::Rate loop_rate(5);//每秒5帧
    while(nh.ok())
    {
        pub.publish(msgpub);
        ROS_INFO("publishing");
        ros::spinOnce();
        loop_rate.sleep();
    }
}