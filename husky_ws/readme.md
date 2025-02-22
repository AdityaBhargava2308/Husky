Instructions to build the workspace: 
	cd husky_ws/
	colcon build
	source install/setup.bash
	
Instruction to open gazebo and robot:
	cd husky_ws/
	source install/setup.bash
	ros2 launch husky_gazebo husky_playpen.launch.py
	
Instruction for nav2:
	cd husky_ws/
	source install/setup.bash
	ros2 launch turtlebot3_navigation2 navigation2.launch.py 

Instruction to run the dynamic obstacle node:
	cd husky_ws/
	source install/setup.bash
	ros2 run dynamic_obs dynamic_obstacle 
	
	
Approach:
	intalling package for husky.
	adding lidar's package.
	making world on gazebo.
	making map using slam toolbox.
	using navigation package of turtlebot3, tune its parameters, modify it to use for husky.
	writing code for dynamic obstacle.
	
Problems faced:
	I wanted to add a dynamic obstacle and not another robot, so I tried using gazebo actor for smooth movement. Although soon I realized it does not posses collision properies. Thus, I took a standard cube and keep spawning and removing it at high rate, such that it appears having a continous motion. Its like discretization a continous motion. Although, it turns out that this process was inefficient and does not behave as expected. This behavious still persists.
	
