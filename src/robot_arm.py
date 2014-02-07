#!/usr/bin/env python
import rospy
from robot_arm.msg import armPos
import SeqEditor

arm = SeqEditor.SeqEditor()

def callback(data):
    global arm
    arm.setPose(data.state, data.dt)
    arm.runPose()


def listener():
    rospy.init_node('robot_arm', anonymous=True)
    rospy.Subscriber("set_position", armPos, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()
