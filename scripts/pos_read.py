#!/usr/bin/env python

import rospy
from std_msgs.msg import String

pub = rospy.Publisher('/ar_pose_marker', String, queue_size=10)
rospy.init_node('ar_data_read')
r = rospy.Rate(10) # 10hz
while not rospy.is_shutdown():
   pub.publish("working?")
   r.sleep()
