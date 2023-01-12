# kmr_description

The package contains xacro description of the KMR iiwa with Intel RealSense D435 cameras and a Robotiq 2F-85 gripper. The package combines description from multiple sources to describe the configuration of the KMR robot at NTNU. The list shows the relevant repositories.

- KMP200 and iiwa14 description is based of the [kmriiwa_ros_stack repo](https://github.com/stoic-roboticist/kmriiwa_ros_stack) by [stoic-roboticist](https://github.com/stoic-roboticist/)
- The gripper description is based of the [roboti1_arg85_description repo](https://github.com/a-price/robotiq_arg85_description) by [a-price](https://github.com/a-price/)
- The RealSense D435 description is retrieved from the official [realsense-ros repo](https://github.com/IntelRealSense/realsense-ros) by [IntelRealSense](https://github.com/IntelRealSense/).

## Usage
The package contains a launch file [`display.launch.py`](./launch/display.launch.py) for visualizing different xacro files and testing joints using the `robot_state_publisher_node` and the `joint_state_publisher_gui_node`

The [rviz directory](./rviz) contains a configuration file for Rviz2.