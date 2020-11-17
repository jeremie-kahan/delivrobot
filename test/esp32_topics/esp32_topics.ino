//===================================
// add to ESP32 Capteurs:

//include ROS

#include <ros.h>
#include <std_msgs/Bool.h>
#include <deliv_robot/Joystick_cmd.h>

ros::NodeHandle nh;

std_msgs::Bool state_sensor;
std_msgs::Bool wall_detection;
deliv_robot::Joystick_cmd axes;

ros::Publisher esp32_sensor("/esp32/state_sensor", &state_sensor);
ros::Publisher esp32_sensor_wall("/esp32/wall_detection", &wall_detection);
ros::Publisher esp32_joystick("/esp32/joystick", &axes);

void setup(void){
  //Initialise ROS
  nh.initNode();
  nh.advertise(esp32_sensor);
  nh.advertise(esp32_sensor_wall);
  nh.advertise(esp32_joystick);
}

void loop(void){
  //ROS
  
  state_sensor.data = true;
  esp32_sensor.publish( &state_sensor);

  //wall_detection.data = false;
  //esp32_sensor_wall.publish( &wall_detection);
  
  delay(5000); //5s
  state_sensor.data = false;
  esp32_sensor.publish( &state_sensor);

  delay(5000); //5s

  //wall_detection.data = true;
  //esp32_sensor_wall.publish( &wall_detection);

  //axes.x = 50;
  //axes.y = 30;
  //esp32_joystick.publish( &axes );
  nh.spinOnce();
}
