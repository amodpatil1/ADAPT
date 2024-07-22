from launch import LaunchDescription
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Find the share directory of the car_description package
    car_description_share = FindPackageShare('car_description').find('car_description')
    
    # Construct the path to the publish_model.launch.py file
    publish_model_launch_file = os.path.join(car_description_share, 'launch', 'publish_model.launch.py')
    
    ros_deep_learning_share = FindPackageShare('ros_deep_learning').find('ros_deep_learning')
    
    # Construct the path to the detectnet.ros2.launch file
    detectnet_launch_file = os.path.join(ros_deep_learning_share, 'launch', 'detectnet.ros2.launch')

    # Find the share directory of the realsense2_camera package
    realsense2_camera_share = FindPackageShare('realsense2_camera').find('realsense2_camera')
    
    # Construct the path to the rs_launch.py file
    rs_launch_file = os.path.join(realsense2_camera_share, 'launch', 'rs_launch.py')

    return LaunchDescription([
        # Include the publish_model.launch.py
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(publish_model_launch_file)
        ),

       
        Node(
            package='adapt_loc',
            executable='localization',
            name='localization'
        ),
        Node(
            package='adapt_roucomp',     
            executable='route',  
            name='routemodule5'
        ),
        Node(
            package='adapt_trajp',
            executable='traj',
            name='trajectory_planner'
        ),
        Node(
            package='adapt_envmod',
            executable='env_mod',
            name='envmod'
        ),
        Node(
            package='adapt_latlongcon',
            executable='pp',
            name='path_tracking'
        ),
        Node(
            package='adapt_behplan',
            executable='behave',
            name='beh'
        ),
        Node(
            package='adapt_transceiver',
            executable='transceiver_node',
            name='transceiver'
        ),
        Node(
            package='adapt_transceiver',
            executable='cpm',
            name='CPM'
        ),
        Node(
            package='ros2_pcan',
            executable='ros2pcan_node',
            name='ros2_pcan'
        )
    ])

