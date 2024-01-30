from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='adapt_envmod',
            executable='env_node',
            name='adapt_envmod'
            
        ), 
    ])