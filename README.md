# README
## Objective
Control robot with DNN
### Procedure 
1. Detect object(karaage or mashmelo)
2. Get pose of object
3. Send pose to robot
4. control robot to grasp 

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

### PC Info 
|Info||
|-|-|
|User|hayashi|
|Password|hayashi|
|IP address|192.168.11.2|

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
![Screenshot from 2023-09-01 16-29-13](https://github.com/YoshitakaSAKATA/MyResearchDocument/assets/118269935/07063aef-3b52-45f4-b7ba-9b9b808a34cd)
[The video of robot running](https://mailkyutechjp-my.sharepoint.com/personal/sakata_yoshitaka414_mail_kyutech_jp/_layouts/15/stream.aspx?id=%2Fpersonal%2Fsakata%5Fyoshitaka414%5Fmail%5Fkyutech%5Fjp%2FDocuments%2FHayashiLab%2FProgress%2FIMG%5F4282%2EMOV&referrer=OfficeHome%2EWeb&referrerScenario=RecentVideo%2EView)

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
[The video of robot running](https://mailkyutechjp-my.sharepoint.com/personal/sakata_yoshitaka414_mail_kyutech_jp/_layouts/15/stream.aspx?id=%2Fpersonal%2Fsakata%5Fyoshitaka414%5Fmail%5Fkyutech%5Fjp%2FDocuments%2FHayashiLab%2FProgress%2FIMG%5F4282%2EMOV&referrer=OfficeHome%2EWeb&referrerScenario=RecentVideo%2EView)
### Run via ROS1
1. Move to workspace
   ```
   cd ~/worksp/camera_ws/src
   ```

2. Download realsense-ros from [Here](https://github.com/IntelRealSense/realsense-ros#installation-instructions) (, and [also](https://github.com/IntelRealSense/realsense-ros/tree/ros1-legacy))
   ```
   git clone https://github.com/IntelRealSense/realsense-ros.git
   cd realsense-ros
   git checkout `git tag | sort -V | grep -P "^2.\d+\.\d+" | tail -1`
   cd ../
   ```
   
3. Build 

3. Error message would be desplayed on terminal, so please install ddynamic_reconfigure
   ```
   sudo apt-get install ros-noetic-ddynamic-reconfigure
   sudo apt update
   ```

4. Build again

5. Source
   ```
   echo "source ~/worksp/camera_ws/devel/setup.bash" >> ~/.bashrc
   source ~/.bashrc
   ```
   
6. Run realsense2_camera using below command
   ```
   roslaunch realsense2_camera rs_camera.launch
   ```

   Run Image View on another terminal
   ```
   rosrun rqt_image_view rqt_image_view
   ```
7. [PointCloud2](https://qiita.com/ReoNagai/items/04dfbcf1f4f3600e8d70)

![Screenshot from 2023-09-01 16-14-14](https://github.com/YoshitakaSAKATA/MyResearchDocument/assets/118269935/2101672c-4005-4e01-a2a4-89b935b260af)

## Test Arducam Multi Camera Adapter Module V2.2 - September 6
Please refer to [Quick start](https://github.com/ArduCAM/RaspberryPi/tree/master/Multi_Camera_Adapter/Multi_Adapter_Board_4Channel)

**Don't get the wrong model when you edit the config.txt!** 
There are 3 cameras, two Camera Module v3(imx708) and one Camera Module v2(imx219). 
When a camera is not recognized, you have to edit sensor number on config.txt.
```
sudo nano /boot/config.txt
```
Please make sure to enter the correct model number.

**This part**
```
dtoverlay="sensor number"
```





## Setup RPi4B - September 8
### RPi Info
   |RPi|Info|
   |----|-------|
   |User|hayashi|
   |Password|hayashi|
   |IP address|192.168.11.3|
   |Port|65530|
1. Test camera module 
2. Setting SSH of RPi4B
   1. enable SSH of RPi
   2. execute below command
      ```
      cd /boot
      sudo mkdir ssh
      ```
      and reboot
      ```
      sudo reboot
      ```
      
   3. Edit sshd_config
      ```
      sudo nano /etc/ssh/sshd_config
      ```
 
      Change this part **from 49512 to 65535 (Don't forget to remove "#"!)**
      ```
      Port 65530
      ```

      and restart ssh
      ```
      sudo /etc/init.d/ssh restart
      ```
    4. PC can connect RPi via SSH with new Port number 
       ```
       ssh hayashi@192.168.11.3 -p 65530
       ```
    5. Make secret key and public key **on PC**
       ```
       ssh-keygen -t rsa -b 4096 -C "sakatayoshitaka1031@gmail.com"
       ```
       You will be asked where to generate the key, so press Enter

    6. Make sure to execute below command **on RPi**
       ```
       mkdir ~/.ssh
       ```
       Send public key **from PC to RPi**
       ```
       cd ~/.ssh
       scp -P 65530 id_rsa.pub hayashi@192.168.11.3:/home/hayashi/.ssh
       ```

       Add id_rsa.pub to authorized_keys **on RPi**
       ```
       cd ~/.ssh/
       cat id_rsa.pub >> authorized_keys
       chmod 600 authorized_keys
       chmod 700 ~/.ssh
       rm ~/.ssh/id_rsa.pub
       ```

    7. Connect with below command
       ```
       ssh hayashi@192.168.11.3 -i hayashi -p 65530
       ```

    8. Change SSH configuration on RPi
       ```
       sudo nano /etc/ssh /sshd_config
       ```

       Change this part 
       ``` conf
       #PermitRootLogin prohibit-password #to "PermitRootLogin no"
       #PasswordAuthentication yes #to "PasswordAuthentication no"
       #PermitEmptyPasswords no #remove "#"
       ```

    9. Make config file **with VScode on PC**
       ```
       Host hayashi
               HostName 192.168.11.3
               User hayashi
               Port 65530
               IdentityFile hayashi
       ```

    10. You can connect RPi with VScode
    
## Send stream to PC - September 11
Please refer to [this document about Picamera2](https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf)

## Send stream to PC with ROS1 - September 26
1. ```
   roscore
   ```
2. On new terminal, go to camera_ws and run program to recieve and publish Image
   ```
   cd ~/worksp/camera_ws/
   rosrun gripper_camera TcpStreamAndPublish.py
   ```
   
3. Connect RPi on SSH and run program to capture and send image to PC with TCP
   ```
   python TcpStreamClient.py
   ```
4. You can see Image on rqt_image
   Images will be stored in **camera_ws/src** as image_YMDHMS.jpg
   ```
   rqt_image_view
   ```
   
## Control gripper 
### Imformation about motor
|Part|Name|
|-|-|
|Stepper Motor|Makerbase mks servo42c v1.0(Nema17)|




## MoveItによるアームのコントロール
1. 以下のコマンドを実行
    ```
    roslaunch arm_controller utarm_api_server.launch arm_ip:=192.168.11.160
    roslaunch utra6_850_moveit_config run_with_utra6_850.launch
    ```

2. 新しくモーションプランニング用のパッケージを作り, 実行 
    /home/hayashi/worksp/utra_ws/src/utra_motion_planning/src/utra_motion_test.pyにある
   ```
   rosrun utra_motion_planning utra_motion_test.py
   ```

   **怪しい動きをしたらすぐに緊急停止ボタンを押す**
