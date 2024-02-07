from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
       Node(
            package='adapt_transmitter',     
            executable='transmitter_node',  
            name= 'transmitter_data'          
            
        ),
       Node(
            package='adapt_loc',
            executable='localization',
            name='localization'
        ),
        
        Node(
            package='adapt_transmitter',     
            executable='cpm',  
            name= 'transmitternode' 
        )    
            
    ])              