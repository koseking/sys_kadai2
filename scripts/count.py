#!/usr/bin/env python
import rospy
import time
from std_msgs.msg import Int32

if __name__ == '__main__':
	rospy.init_node('count')
	pub = rospy.Publisher('count_down', Int32, queue_size=1)
	rate = rospy.Rate(10)
	n = 10000
        a = 0
	while not rospy.is_shutdown():
		n = n - a
                a += 1 
		time.sleep(3) 
		pub.publish(n)
		rate.sleep()

