#include "ros.h"
#include "std_msgs/Bool.h"

const int potPin = 36;
int potValue = 0;
ros::NodeHandle nh;

std_msgs::Bool str_msg;
ros::Publisher chatter("/esp32/wall_detector", &str_msg);

void setup() {
  // put your setup code here, to run once:
  nh.initNode();
  nh.advertise(chatter);
}

void loop() {
  // put your main code here, to run repeatedly:
  potValue = analogRead(potPin);
  if (potValue<900){
    str_msg.data = true;
  }
  else{
    str_msg.data = false;
  }
  chatter.publish(&str_msg);
  nh.spinOnce();
  delay(500);
}
