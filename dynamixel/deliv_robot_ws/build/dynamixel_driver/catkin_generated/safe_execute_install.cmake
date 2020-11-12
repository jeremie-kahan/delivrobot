execute_process(COMMAND "/home/student/Documents/deliv_robot_ws/build/dynamixel_driver/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/student/Documents/deliv_robot_ws/build/dynamixel_driver/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
