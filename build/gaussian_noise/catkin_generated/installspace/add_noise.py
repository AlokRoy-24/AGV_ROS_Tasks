#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import random

pub_gauss=rospy.Publisher('chatter',Twist,queue_size=10)
var=Twist()

def callback(data):
    var.linear.x=(data.linear.x+random.random())
    var.linear.y=(data.linear.y+random.random())
    var.linear.z=(data.linear.z+random.random())
    pub_gauss.publish(var)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('cmd_vel', Twist, callback)
    rospy.spin()

if __name__ == '__main__':
      listener()