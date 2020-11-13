#!/usr/bin/env python

import rospy
import sys
from std_msgs.msg import Float64 


class dynamixel_commande:
    OUVERT = True
    Position = 0
    def __init__(self):
        rospy.init_node('Dynamixel_commande', anonymous=True)
        #rospy.Subscriber("/tilt_controller/command", Float64, self.callback)
        
        self.pub_position = rospy.Publisher("/tilt_controller/command", Float64, queue_size = 10)

        rospy.loginfo("[dynamixel_commande] node started")

        

    def callback(self, data):
        #while not is_shutdown:
        #rospy.loginfo("L'altitude est de: %f", data.altitude)
        rospy.loginfo("la position du moteur est a: " + str(data.data))
        self.set_position(0)
         

    def set_position(self,position):
        #rostopic pub -1 /dual_motor_controller/command std_msgs/Float64 -- 1.5
        Position = position
        try:
            for i in range(0,1000):
                self.pub_position.publish(position)
            rospy.loginfo("Le moteur tourne")
        
        except rospy.ServiceException as e:
            rospy.logwarn("Service call failed: %s"%e)

        

if __name__ == '__main__':
    position = 0

    if len(sys.argv) >= 1:
            position=float(sys.argv[1])
            
    try:
        command = dynamixel_commande()
        rospy.sleep(1)
        command.set_position(position)

    except rospy.ROSInterruptException:
        pass
