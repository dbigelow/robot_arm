#include "ros/ros.h"
#include "robot_arm/armPos.h"
#include <iostream>

using namespace std; 

int main(int argc, char *argv[])
{
	ros::init(argc, argv, "setter");

	ros::NodeHandle n;

	ros::Publisher arm_pub = n.advertise<robot_arm::armPos>("set_position", 1000);

	robot_arm::armPos msg1;
	robot_arm::armPos msg2;

	msg1.state.push_back(512);
	msg1.state.push_back(512);
	msg1.state.push_back(800);
	msg1.state.push_back(724);
	msg1.state.push_back(512);
	msg1.dt = 700;

	msg2.state.push_back(900);
	msg2.state.push_back(512);
	msg2.state.push_back(512);
	msg2.state.push_back(515);
	msg2.state.push_back(90);
	msg2.dt = 700;

	ros::Rate loop_rate(.5);

	while(ros::ok())
	{
		arm_pub.publish(msg1);
		ros::spinOnce();
		loop_rate.sleep();

		arm_pub.publish(msg2);
		ros::spinOnce();
		loop_rate.sleep();
	}
	return 0;
}