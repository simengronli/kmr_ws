# kmr_bringup

Package containing base funcitonality for starting the robot with some example scrips. Includes three launch files described below.

**ROS 2 Version: Foxy**

## [`bringup.launch.py`](./launch/bringup.launch.py)
Bring up rviz and the relevant sensors to be viewed. This requires the simulator to be running and publishing data on relevant topics.

## [`slam_toolbox.launch.py`](./launch/slam_toolbox.launch.py)
Example of SLAM using the KMR in Isaac Sim with ROS 2

Startup procedure:
1. Start simulation in Isaac Sim
2. In one terminal, launch [kmr_concatenator](../kmr_concatenator/launch/concatenator.launch.py) as described in the [readme](../kmr_concatenator/README.md) and wait for the message "`Initialialized laser scan syncronizer`" from the `concatenator_node`. This should take about 3 seconds.
3. When that message is received launch [`slam_toolbox.launch.py](./launch/slam_toolbox.launch.py) in a second terminal.
4. Drive the robot around the environment using e.g. the [teleop_twist_keyboard package](https://index.ros.org/r/teleop_twist_keyboard/) from a third terminal.


## [`navigation.launch.py`](./launch/navigation.launch.py)
Example using Navigation 2 in Isaac Sim with the KMR.

The map has to match the environment the robot is placed in. This can be specified on line 17 in [`navigation.launch.py`](./launch/navigation.launch.py). Parameter files are located in the [config](./config) directory and should be specified on line 24 in [`navigation.launch.py`](./launch/navigation.launch.py).

Startup procedure:
1. Start simulation in Isaac Sim
2. In one terminal, launch [kmr_concatenator](../kmr_concatenator/launch/concatenator.launch.py) as described in the [readme](../kmr_concatenator/README.md) and wait for the message "`Initialialized laser scan syncronizer`" from the `concatenator_node`. This should take about 3 seconds.
3. When that message is received launch [`navigation.launch.py](./launch/navigation.launch.py) in a second terminal.
4. Rviz should show up and the initial pose is already set in the [params file](./config/navigation_params.yaml). Send new goal poses from Rviz and the robot should move in Isaac Sim

TODO