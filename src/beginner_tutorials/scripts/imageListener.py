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

def callback(data):
    # cv2.imshow('listener',data.data)
    img=data.data
    array=np.frombuffer(img, dtype=np.uint8)
    array=array.reshape(512,512,3)
    cv2.imshow('img',array)
    cv2.waitKey(1)
    # cv2.destroyAllWindows()

def imagelistener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/camera/image_raw',Image,callback)
    rospy.spin()

if __name__=='__main__':
    imagelistener()