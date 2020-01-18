#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

<<<<<<< HEAD
def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
=======
pub = rospy.Publisher('/ar_pose_marker', String, queue_size=10)
rospy.init_node('ar_data_read')
r = rospy.Rate(10) # 10hz
while not rospy.is_shutdown():
   pub.publish("working?")
   r.sleep()
>>>>>>> 4a63e289faad0b9407858ca80323290520fd143e
