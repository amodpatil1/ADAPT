from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='adapt_envmod',
            executable='env_mod',
            name='envmod'
        ),
        Node(
            package='adapt_trajp',
            executable='traj',
            name='trajectory_planner'
        ),
        Node(
            package='adapt_loc',
            executable='localization',
            name='localization'
        ),
        Node(
            package='adapt_transceiver',
            executable='transceiver_node',
            name='transceiver'
        ),
        Node(
            package='ros2_pcan',
            executable='ros2pcan_node',
            name='ros2pcan'
        )

    ])

