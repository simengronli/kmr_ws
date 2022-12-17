# kmr_bringup

Package containing base funcitonality for starting the robot with some example scrips. Includes three launch files described below.

## [`bringup.launch.py`](./launch/bringup.launch.py)
Bring up rviz and the relevant sensors to be viewed

## [`slam_toolbox.launch.py`](./launch/slam_toolbox.launch.py)
Example of slam using the KMR in isaac sim with ros2

Startup procedure:
1. Start simulation in Isaac Sim
2. In one terminal, launch [kmr_concatenator](../kmr_concatenator/launch/concatenator.launch.py) as described in the [readme](../kmr_concatenator/README.md) and wait for the message "`Initialialized laser scan syncronizer`" from the `concatenator_node`. This should take about 3 seconds.
3. When that message is received launch [`slam_toolbox.launch.py](./launch/slam_toolbox.launch.py) in a second terminal.
4. Drive the robot around the environment using e.g. the [teleop_twist_keyboard package](https://index.ros.org/r/teleop_twist_keyboard/) from a third terminal.


## [`navigation.launch.py`](./launch/navigation.launch.py)
Navigation example

TODO