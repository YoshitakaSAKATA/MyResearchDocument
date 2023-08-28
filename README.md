# README
## Prepare the PC for research
1. install ubuntu 20.04 LTS on new PC.
2. update and upgrade
3. install ROS-noetic
4. install GPU softwares
5. install miniconda3
6. The version of gazebo is 11.11.0
7. install [ros_control](http://wiki.ros.org/ros_control)
8. install [ros_noetic_moveit](https://moveit.ros.org/install/)
9. make workspace contains utra_ros and camera_ws
10. In utra_ros, obtain [utra_ros packages ](https://github.com/UmbraTek/ut_arm_ros)
11. 
 
## how to build multiple ROS1 workspace
steps
1. create main folder to keep all the workspace e.g. worksp folder
```
mkdir worksp
```

2. head inside the worksp folder
```
cd worksp
```

3. create the first ros workspace and its src folder e.g. named robot_ws
```
mkdir -p robot_ws/src
```

4. git, make or create the ros package as you want
5. build the ros workspace

6. add the source to the .bashrc and source it
```
source ~/worksp/robot_ws/devel/setup.bash
```

7. to build another ros workspace alongside with the first worksp, repeat from the step 3
but when creating the second ros workspace, create in the worksp folder

## Run Rviz and connect with arm(Moveit and ros_industrial)
1.  ```
    roslaunch arm_controller utarm_api_server.launch arm_ip:=192.168.11.160
    ```

2.  ```
    roslaunch utra6_850_moveit_config run_with_utra6_850.launch 
    ```

3.  ```
    rosservice call /utsrv/connect "192.168.11.160" 
    ```
4. (Essensial!) You must open "Panels" ->"utra_rviz" -> "utra_panel" and check "Enable" and push "resume"
 
