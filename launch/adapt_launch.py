from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='adapt_envmod',  #your package name
            namespace='environment', #custom     
            executable='env_node',   #the entry point
            name= 'envmod'           # Node name
            
        ),
        
        Node(
            package='adapt_roucomp',
            namespace='routecomputer', 
            executable='route_node',
            name='roucomp'
            
        ),
        Node(
            package='adapt_ui',
            namespace='ui1',
            executable='show',
            name='Pubsub1'
        ),
 
        
        Node(
            package='adapt_behplan',
            namespace='behaviour',
            executable='behaviour_node',
            name='behplan'
        ),

        Node(
            package='adapt_trnsmtr', 
            namespace='transmitter',  
            executable='trnsmtr_node',  
            name= 'trnsmtr_data'          
            
        ),
        Node(
            package='adapt_latlongcon',  
            namespace='control',            
            executable='latlong_node',   
            name= 'latlongcon'           
            
        )
                Node(
            package='adapt_lanboun',  
            namespace='lanedetect',            
            executable='lane_detection_node',   
            name= 'lane_detection'           
            
        )
    ])