#! /usr/bin/python
# -*- coding: utf-8 -*-
import rospy
import gait2
import matplotlib.pyplot as plt
from std_msgs.msg import Float64
def talker():
    flf = rospy.Publisher('/spotmicroai/front_left_foot_position_controller/command', Float64, queue_size=1)
    fll = rospy.Publisher('/spotmicroai/front_left_leg_position_controller/command', Float64, queue_size=1)
    fls = rospy.Publisher('/spotmicroai/front_left_shoulder_position_controller/command', Float64, queue_size=1)

    frf = rospy.Publisher('/spotmicroai/front_right_foot_position_controller/command', Float64, queue_size=1)
    frl = rospy.Publisher('/spotmicroai/front_right_leg_position_controller/command', Float64, queue_size=1)
    frs = rospy.Publisher('/spotmicroai/front_left_shoulder_position_controller/command', Float64, queue_size=1)

    rlf = rospy.Publisher('/spotmicroai/rear_left_foot_position_controller/command', Float64, queue_size=1)
    rll = rospy.Publisher('/spotmicroai/rear_left_leg_position_controller/command', Float64, queue_size=1)
    rls = rospy.Publisher('/spotmicroai/front_left_shoulder_position_controller/command', Float64, queue_size=1)

    rrf = rospy.Publisher('/spotmicroai/rear_right_foot_position_controller/command', Float64, queue_size=1)
    rrl = rospy.Publisher('/spotmicroai/rear_right_leg_position_controller/command', Float64, queue_size=1)
    rrs = rospy.Publisher('/spotmicroai/front_left_shoulder_position_controller/command', Float64, queue_size=1)

    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(40) # 10hz
    itrs=len(gait2.beta_list)
    index=0
    while not rospy.is_shutdown() or index<=itrs:
	flf1 = gait2.gamma_list[index]
	fll1 = gait2.beta_list[index]
	fls1=gait2.alpha_list[index]

	frf1 = gait2.gamma_list2[index]
	frl1 = gait2.beta_list2[index]
	frs1=gait2.alpha_list2[index]

	rlf1 = gait2.gamma_list3[index]
	rll1 = gait2.beta_list3[index]
	rls1=gait2.alpha_list3[index]

	rrf1 = gait2.gamma_list4[index]
	rrl1 = gait2.beta_list4[index]
	rrs1=gait2.alpha_list4[index]
	

	#rospy.loginfo(left_bottom)
        #rospy.loginfo(left_top)
	flf.publish(flf1)
	fll.publish(fll1)
	fls.publish(fls1)

	frf.publish(frf1)
	frl.publish(frl1)
	frs.publish(frs1)

	rlf.publish(rlf1)
	rll.publish(rll1)
	rls.publish(rls1)

	rrf.publish(rrf1)
	rrl.publish(rrl1)
	rrs.publish(rrs1)

	index+=1
	if index>=itrs:
		index=0
	#print(gait2.beta_list)
        rate.sleep()
 
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
