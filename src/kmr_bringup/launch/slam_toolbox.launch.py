import os
from ament_index_python.packages import get_package_share_path

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import Command, LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    kmr_bringup_path = get_package_share_path('kmr_bringup')
    rviz_config_path = kmr_bringup_path / 'rviz/bringup.rviz'
    slam_toolbox_launch_file_dir = os.path.join(get_package_share_path('slam_toolbox'), 'launch')

    rviz_arg = DeclareLaunchArgument(name='rvizconfig', default_value=str(rviz_config_path),
                                     description='Absolute path to rviz config file')

    slam_toolbox_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([slam_toolbox_launch_file_dir, '/online_async_launch.py']),
        launch_arguments={
            'params_file': os.path.join(kmr_bringup_path, 'config/mapper_params_online_async.yaml'),
        }.items(),
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', LaunchConfiguration('rvizconfig')],
    )

    return LaunchDescription([
        slam_toolbox_launch,
        rviz_arg,
        rviz_node
    ])
