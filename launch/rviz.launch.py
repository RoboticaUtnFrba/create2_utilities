#!/usr/bin/env python

# Copyright 2021 Emiliano Javier Borghi Orue.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Launch Webots iRobot Create 2 driver."""

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions.path_join_substitution import PathJoinSubstitution
from launch_ros.actions import Node


def generate_launch_description():
    package_dir = get_package_share_directory('create2_utilities')

    rviz_config = PathJoinSubstitution([package_dir, 'resource', 'bringup.rviz'])

    # Nodes

    rviz2 = Node(
        package='rviz2',
        executable='rviz2',
        output='log',
        arguments=['--display-config=' + rviz_config.perform(None)],
    )

    return LaunchDescription([
        # Nodes
        rviz2,
    ])
