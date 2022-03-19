#! /usr/bin/env python
import queue
import rospy 
from std_msgs.msg import Header 
from sensor_msgs.msg import Image 
import os 
import cv2 
import numpy as np 
import time 

IMAGE_WIDTH=1241 
IMAGE_HEIGHT=376 

rospy.init_node("image_publisher", anonymous=True)
image_publisher=rospy.Publisher('/camera/image_raw',Image, queue_size=10)
def publish_image(imgdata):
    image_temp=Image()
    header=Header(stamp=rospy.Time.now())
    header.frame_id='map'
    # image_temp.height=IMAGE_HEIGHT
    # image_temp.width=IMAGE_WIDTH 
    # image_temp.encoding='rgb8'
    image_temp.data=np.array(imgdata).tobytes()#有这个用法吗
    image_temp.header=header
    # image_temp.step=1241*3 
    image_publisher.publish(image_temp)
while not rospy.is_shutdown():
    img=cv2.imread('/home/lee/lena.jpg')
    # cv2.imshow('img',img)
    # cv2.waitKey(30)
    publish_image(img)
    rospy.Rate(10).sleep()