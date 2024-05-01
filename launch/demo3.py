from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='adapt_behplan',     
            executable='beh_node',  
            name= 'beh_plan' 
        ),
        Node(
            package='adapt_roucomp',     
            executable='route_node',  
            name= 'route_comp' 
        ),
        Node(
            package='adapt_latloncon',     
            executable='latlong',  
            name= 'latlong_node' 
        )                                 
            
    ])              
