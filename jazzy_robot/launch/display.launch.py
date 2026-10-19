from pathlib import Path

from launch import LaunchDescription
from launch_ros.actions import Node


folder = Path(__file__).resolve().parent.parent

robot_description = (folder / "urdf" / "jazzy_wheeled_robot.urdf").read_text()

rviz_config = folder / "rviz" / "view.rviz"

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            parameters=[{
                "robot_description": robot_description
            }],
            output="screen",
        ),
        Node(
            package="joint_state_publisher_gui",
            executable="joint_state_publisher_gui",
            output="screen",
        ),
        Node(
            package="rviz2",
            executable="rviz2",
            arguments=(
                ["-d", str(rviz_config)]
                if rviz_config.exists() else []
            ),
            output="screen",
        ),
    ])