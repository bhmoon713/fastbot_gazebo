import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.actions import OpaqueFunction

def launch_setup(context, *args, **kwargs):

    entity_name = LaunchConfiguration('robot_name').perform(context)
    x_spawn = LaunchConfiguration('x_spawn').perform(context)
    y_spawn = LaunchConfiguration('y_spawn').perform(context)
    z_spawn = LaunchConfiguration('z_spawn').perform(context)
    roll_spawn = LaunchConfiguration('roll_spawn').perform(context)
    pitch_spawn = LaunchConfiguration('pitch_spawn').perform(context)
    yaw_spawn = LaunchConfiguration('yaw_spawn').perform(context)

    # Position and orientation
    # [X, Y, Z]
    position = [x_spawn, y_spawn, z_spawn]
    # [Roll, Pitch, Yaw]
    orientation = [roll_spawn, pitch_spawn, yaw_spawn]
    robot_description_topic_name = "/" + entity_name + "_robot_description"
    robot_state_publisher_name= entity_name + "_robot_state_publisher"
    spawn_node_name = entity_name + "_spawn_entity"

    # Spawn ROBOT Set Gazebo
    spawn_robot = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        name=spawn_node_name,
        output='screen',
        emulate_tty=True,
        arguments=['-entity',
                   entity_name,
                   '-x', str(position[0]), '-y', str(position[1]
                                                     ), '-z', str(position[2]),
                   '-R', str(orientation[0]), '-P', str(orientation[1]
                                                        ), '-Y', str(orientation[2]),
                   '-topic', robot_description_topic_name
                   ],
        remappings=[("/robot_state_publisher", robot_state_publisher_name)
                    ]
    )


    return [spawn_robot]


def generate_launch_description(): 

    robot_name_arg = DeclareLaunchArgument('robot_name', default_value='fastbot')
    x_spawn_arg = DeclareLaunchArgument('x_spawn', default_value='0.0')
    y_spawn_arg = DeclareLaunchArgument('y_spawn', default_value='0.0')
    z_spawn_arg = DeclareLaunchArgument('z_spawn', default_value='0.0')
    roll_spawn_arg = DeclareLaunchArgument('roll_spawn', default_value='0.0')
    pitch_spawn_arg = DeclareLaunchArgument('pitch_spawn', default_value='0.0')
    yaw_spawn_arg = DeclareLaunchArgument('yaw_spawn', default_value='0.0')


    return LaunchDescription([
        robot_name_arg,
        x_spawn_arg,
        y_spawn_arg, 
        z_spawn_arg,
        roll_spawn_arg,
        pitch_spawn_arg,
        yaw_spawn_arg,
        OpaqueFunction(function = launch_setup)
        ])