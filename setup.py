from glob import glob
import os

from setuptools import setup

package_name = 'create2_utilities'

data_files = []
# Install marker file in the package index
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
# Include our package.xml file`
data_files.append(('share/' + package_name, ['package.xml']))
# Include all launch files
data_files.append((os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')))
# Configuration files
data_files.append(('share/' + package_name + '/resource', [
    'resource/bringup.rviz',
]))


setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    author='Emiliano J. Borghi Orue',
    author_email='eborghiorue@frba.utn.edu.ar',
    maintainer='Emiliano J. Borghi Orue',
    maintainer_email='eborghiorue@frba.utn.edu.ar',
    description='ROS 2 package for the iRobot Create 2 with graphical and testing tools.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
