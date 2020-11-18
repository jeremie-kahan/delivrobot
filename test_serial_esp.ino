#include "ros.h"
#include "std_msgs/String.h"

const int potPin = 36;
int potValue = 0;
ros::NodeHandle nh;

std_msgs::String str_msg;
ros::Publisher chatter("chatter", &str_msg);

char hello[4] = "OFF";

void setup() {
  // put your setup code here, to run once:
  nh.initNode();
  nh.advertise(chatter);
}

void loop() {
  // put your main code here, to run repeatedly:
  potValue = analogRead(potPin);
  if (potValue <3000){
    hello == "ON ";
  }
  else{
    hello == "OFF";
  }
  str_msg.data = hello;
  chatter.publish(&str_msg);
  nh.spinOnce();
  delay(500);
}
