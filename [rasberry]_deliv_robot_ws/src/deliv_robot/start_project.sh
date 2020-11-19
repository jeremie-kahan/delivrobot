#!/bin/bash
#this script will execute all the commands to start the projet
#Usage: ./start_nodes

#set all the permission
echo ===================================================== Autorisation des ports USB ======================================================================
sudo chmod 666 /dev/ttyUSB0
sudo chmod 666 /dev/ttyUSB1
sudo chmod 666 /dev/ttyACM0
sudo chmod 666 /dev/ttyACM1
#do a source
source ~/deliv_robot_ws/devel/setup.bash

#execute the launch file
echo ===================================================== Execute  roslaunch ======================================================================
roslaunch deliv_robot all.launch
