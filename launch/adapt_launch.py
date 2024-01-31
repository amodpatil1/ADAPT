from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='adapt_envmod',  
            
            executable='env_node',   
            name= 'envmod'           
            
        ),
        
        Node(
            package='adapt_roucomp',
            
            executable='route_node',
            name='roucomp'
            
        ),
        Node(
            package='adapt_ui',
            
            executable='show',
            name='UI_1'
        ),
 
        
        Node(
            package='adapt_behplan',
            executable='behaviour_node',
            name='behplan'
        ),

        Node(
            package='adapt_trnsmtr', 
             
            executable='transmitter_node',  
            name= 'transmitter_data'          
            
        ),
        Node(
            package='adapt_latlongcon',  
                        
            executable='latlong_node',   
            name= 'latlongcon'           
            
        )
        Node(
            package='adapt_lanboun',           
            executable='lane_detection_node',   
            name= 'lane_detection'           
            
        )
    ])