# KMR_WS

This is the main repository for development of a ROS 2 stack for the KUKA KMR iiwa used in NVIDIA Isaac Sim for my Master's Thesis at NTNU Fall of 2022.

The workspace contains a [kmr_description package](./src/kmr_description/) describing the robot and a [kmr_bringup package](./src/kmr_bringup/) for doing SLAM and navigation tasks. The [kmr_concatenator package](./src/kmr_concatenator/) is borrowed from [MortenMDahl](https://github.com/MortenMDahl)'s repo [kmriiwa_ws_devel](https://github.com/MortenMDahl/kmriiwa_ws_devel).

The system has been developed and tested with the following specs
- Ubuntu 20.04
- ROS 2 Foxy Firzroy
- [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac-sim)

The system was developed using [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac-sim) and not Gazebo. Modifications can be made for the packages to work, however a repository containing related extensions for Isaac Sim has been created [here](https://github.com/jorgenmyrvold/omniverse-extensions).

## Quick start
**Requires and instance of Isaac Sim to be running and with the KMR Loader extension from the [omniverse-extensions repo](https://github.com/jorgenmyrvold/omniverse-extensions)**

Step by step description to launch SLAM and Navigation systems are described in the [kmr_bringup readme](./src/kmr_bringup/README.md).

![](./images/kmr_in_warehouse.png)