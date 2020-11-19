#!/usr/bin/env python

import rospy
import sys
from std_msgs.msg import Float64, Bool,String
from deliv_robot.msg import Joystick_cmd
from geometry_msgs.msg import Twist


class serial_translator:
    
    def __init__(self):
        rospy.init_node('serial_translator', anonymous=True)

        #Publishers   
        self.pub_sensor = rospy.Publisher("/master/state_sensor", Bool, queue_size = 10)
        self.pub_wall = rospy.Publisher("/master/wall", Bool, queue_size = 10)
        self.pub_joystick = rospy.Publisher("/master/joystick", Twist, queue_size = 10)

        rospy.sleep(1)
        rospy.loginfo("[serial_translator] node started")

        #Subscribers
        rospy.Subscriber("/chatter", String, self.callback)
        rospy.Subscriber("/esp32/state_sensor", Bool, self.sensor_callback)
        rospy.Subscriber("/esp32/wall_detector", Bool, self.wall_callback)
        rospy.Subscriber("/esp32/joystick", Joystick_cmd, self.joystick_callback)


        rospy.spin()

       
    def callback(self,data):
        """
        when receive a topic [/card/<...>], publish the proper topic "/master/<...>"
        """
      
        try:
            rospy.loginfo("from ESP32 : %s",data.data)
        except rospy.ServiceException as e:
            rospy.logwarn("Service call failed: %s"%e)

    def sensor_callback(self,data):
        """
        when receive a topic [/card/<...>], publish the proper topic "/master/<...>"
        """
        #rospy.loginfo("message receive from ESP32/state_sensor")
        self.pub_sensor.publish(data.data)           

    def wall_callback(self,data):
        """
        when receive a topic [/card/<...>], publish the proper topic "/master/<...>"
        """
        #rospy.loginfo("message receive from ESP32/wall_detection")
        self.pub_wall.publish(data.data)

    def joystick_callback(self,data):
        """
        when receive a topic [/card/<...>], publish the proper topic "/master/<...>"
        """
        #rospy.loginfo("message receive from ESP32/joystick: %d,%d", data.x,data.y)
        msg = Twist()
	#
        msg.linear.x = int( (data.x )/0.440)
        msg.linear.y = int((data.y )/0.440)
        self.pub_joystick.publish(msg)

if __name__ == '__main__':
    
    try:
        translate = serial_translator()
        
    except rospy.ROSInterruptException:
        pass
