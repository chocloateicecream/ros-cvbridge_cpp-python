#! /usr/bin/env python 
import rospy 
import queue 
import cv2 
from std_msgs.msg import Header 
from sensor_msgs.msg import Image

import os 
import cv2 
import numpy as np 
import time 
import cv_bridge

def callback(data):
    img=data.data
    # cv2.imshow('img',img)
    array=np.frombuffer(img, dtype=np.uint8)
    array=array.reshape(512,512,3)   
    cv2.imshow('img',array) 
    cv2.waitKey(1)
    # cv2.destroyAllWindows()

def imagelistener():
    rospy.init_node('listener',anonymous=True)
    rospy.Subscriber("camera/image",Image,callback)
    rospy.spin()

if __name__=='__main__':
    imagelistener()
