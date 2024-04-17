from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
       Node(
            package='adapt_envmod',     
            executable='map',  
            name= 'mapping'              
        ),
       Node(
            package='adapt_loc',
            executable='localization',
            name='localization'
        ),
        
        Node(
            package='adapt_transceiver',     
            executable='transceiver_node',  
            name= 'transceiver' 
        ),
        Node(
            package='adapt_vi',     
            executable='transceiver_node',  
            name= 'transceiver' 
        ) ,
        Node(
            package='adapt_mi',     
            executable='transceiver_node',  
            name= 'transceiver' 
        ),
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
            package='adapt_livtrac',     
            executable='livetrac_node',  
            name= 'livetracker' 
        ),
        Node(
            package='adapt_latloncon',     
            executable='latlong',  
            name= 'latlong_node' 
        )                                 
            
    ])              