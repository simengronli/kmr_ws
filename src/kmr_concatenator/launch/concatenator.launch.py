# Copyright 2020 Morten Melby Dahl.
# Copyright 2020 Norwegian University of Science and Technology.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from launch import LaunchDescription
import launch_ros.actions
import sys


def generate_launch_description(argv=sys.argv[1:]):

    # Simulated is 'true' if the KMR is simulated in Gazebo. 
    # If true - 3D coordinates, if false - 2D coordinates from laser scanners.
    simulated = 'true'

    return LaunchDescription([
        launch_ros.actions.Node(
            package="kmr_concatenator",
            executable="concatenator_node.py",
            arguments=['-sim', simulated],
            parameters=[{'use_sim_time': True},],
            output="screen",
            emulate_tty = True,
           ),
           
        launch_ros.actions.Node(
            package="pointcloud_to_laserscan",
            executable="pointcloud_to_laserscan_node",
            name="pointcloud_to_laserscan",
            output="screen",
            parameters=[{'use_sim_time': True}, 
            		    {'range_max' : 30.0},
            		    {'range_min' : 0.4}],
            remappings=[('cloud_in', 'pc_concatenated'),
                        # ('scan', 'scan')]
                        ('scan', 'scan_concatenated')]
            )
    ])
