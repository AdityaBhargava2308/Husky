from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
import launch.actions
import launch_ros.actions


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    
    return LaunchDescription([
        launch_ros.actions.Node(
            package='slam_gmapping',  # Ensure this is the correct package in ROS 2
            executable='slam_gmapping',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time}]
        ),
    ])
