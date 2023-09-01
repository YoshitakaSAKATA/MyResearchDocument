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
11. Install [Realsense SDK and Libraries](https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md)
 
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
echo "source ~/worksp/robot_ws/devel/setup.bash" >> ~/.bashrc
```

7. to build another ros workspace alongside with the first worksp, repeat from the step 3
but when creating the second ros workspace, create in the worksp folder

## August 28th - Run Rviz and connect with arm(Moveit and ros_industrial)
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

## September 1st - Install and update Realsense package
1. Register the server's public key
   ```
   sudo mkdir -p /etc/apt/keyrings
   curl -sSf https://librealsense.intel.com/Debian/librealsense.pgp | sudo tee /etc/apt/keyrings/librealsense.pgp > /dev/null
   ```
   Make sure apt HTTPS support is installed
   ```
   sudo apt-get install apt-transport-https
   ```
2. Add the server to the list of repositories
   ```
   echo "deb [signed-by=/etc/apt/keyrings/librealsense.pgp] https://librealsense.intel.com/Debian/apt-repo `lsb_release -cs` main" | \     sudo tee /etc/apt/sources.list.d/librealsense.list
   
   ```
3. Update and Upgrade
   ```
   sudo apt update
   sudo apt upgrade
   ```

4. Install libraries
   ```
   sudo apt-get install librealsense2-dkms
   sudo apt-get install librealsense2-utils
   ```

5. You can connect and run Realsense with below command
   ```
   realsense-viewer
   ```
   

![Screenshot from 2023-09-01 15-12-07](https://github.com/YoshitakaSAKATA/MyResearchDocument/assets/118269935/1cceff5e-6161-46d1-aa2c-1ae07d36488e)

