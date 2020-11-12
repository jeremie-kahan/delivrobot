#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64


class dynamixel_commande:
    def __init__(self):
        rospy.init_node('Dynamixel_commande', anonymous=True)
        #rospy.Subscriber("/bebop/fix", NavSatFix, self.callback)
        rospy.Subscriber("/tilt_controller/command", Ardrone3PilotingStateAltitudeChanged, self.callback)

        self.pub_position = rospy.Publisher("/tilt_controller/command", Float64, queue_size = 10)
        rospy.spin()

    def callback(self, data):
        #while not is_shutdown:
        #rospy.loginfo("L'altitude est de: %f", data.altitude)
        rospy.loginfo("L'altitude est de: " + str(data.altitude))
        

    def set_command(self, position):
        self.pub_position.publish(position)   

if __name__ == '__main__':
    try:
        Altitude()
    except rospy.ROSInterruptException:
        pass