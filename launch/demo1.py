from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
       
        Node(
            package='adapt_vi',     
            executable='gvi_node',  
            name= 'vi' 
        ) ,
        Node(
            package='adapt_spotsl',
            executable='spotsl_node',
            name='spotsl'
        ) ,
        Node(
            package='adapt_inf_spotupd',
            executable='spot_upd2',
            name='adapt_inf_spotupd'
        ) ,
        Node(
            package='adapt_inf_trans',     
            executable='inf_trans1',  
            name= 'inf_trans1' 
        ) 

                                
            
    ]) 
