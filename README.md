# ADAPT OVERVIEW
Welcome to the main repository of **ADAPT** System. This repository will help you navigate through our organization repositories and hopefully provide a comprehensive understanding of the system architecture and breifly describe components functionality.

### **Question Zero:**
To better understand how this project came to life and what ideas are behined it, let's take a look at our **Question Zero**, in which we try to answer the following about our project; What, For Whom, Where, Why, How:

> :bulb: **Question Zero:** *How can we design an infrastructure-based End2End parking solution for all people arriving with an Autonomous vehicle into the covered urban area, to eliminate the distance traveled & effort required for parking, and reduce emissions, by integrating the leading edge technologies in communication, sensing infrastructure, and autonomous driving?*

### Use Case: 
Parking Autonomously to the Nearest Feasible Parking Spot

* **Main Actors:** Ego Vehicle, Infrastructure

* **Preconditions:**  
 1. Infrastructure monitors parking spots in the vicinity.
 2. User is at their destination.

* **Success Guarantee:** EV parked at the selected spot according to the user preferences.

* **Steps:**  
    1. User starts the process by selecting desired preferences on the VI.
    2. EV initiates communication with infrastructure for parking spots list.
    3. EV receives available spot data from infrastructure.
    4. EV sends confirmation to infrastructure about the chosen spot.
    5. EV selects best route to the parking spot.
    6. EV drives autonomously and parks at the spot.
    7. User can live track his EV using the MI

# UML Diagrams 

## [Acivity Diagram ](https://git.hs-coburg.de/ADAPT/adapt_main/src/branch/main/images/activity_diagram.png)
This diagram outlines the interaction between the autonomous vehicle (referred to as the EV) and the infrastructure from the point where the user commands the EV to park. The EV sends a request for available spots and receives a list from the infrastructure, which also makes the selected spot unavailable to others. The EV then computes a feasible path and begins navigating. The process takes into account obstacles, updating the path as necessary. Behavior planning and control are involved in navigating to the location, culminating in the vehicle parking itself assuming no objects are present in the parking space.

> :memo: **Note:** Diagram is named **Acivity Diagram** the `images` folder. 
## [State Diagram ](https://git.hs-coburg.de/ADAPT/adapt_main/src/branch/main/images/State_Diagram.jpg)
This diagram depicts the various states that an Electric Vehicle (EV) goes through during the process of finding and parking in a parking spot. The process begins when the car arrives at the user destination and enters the idle state, where it locks the door and communicates with the infrastructure to obtain a parking spot. Next, it transitions to the drive state, where it processes data for control and object detection while en route to the parking spot. If an obstacle is detected, it will not proceed to parking. Once near the parking spot, it checks for accessibility, and if it's suitable, the car parks itself. Finally, when the car is in the parking spot, it stops, signaling that it has parked.

> :memo: **Note:** Diagram is named **State Diagram** the `images` folder. 
## [Sequence  Diagram ](https://git.hs-coburg.de/ADAPT/adapt_main/src/branch/main/images/sequence_diagram.png)
This sequence diagram illustrates the communication flow between the autonomous vehicle, the infrastructure, and other system components during the parking process. It starts with the vehicle requesting localization information, selecting a parking spot, and the infrastructure acknowledging this selection. The vehicle then receives localization data from GNSS (Global Navigation Satellite System) and digital maps, and the parking process is executed based on this data. The diagram shows a sequence of communications, including the transmission of the vehicle's location, user preferences, and the selected parking spot's location, which are crucial for the vehicle's navigation and parking operation.

> :memo: **Note:** Diagram is named **Sequence Diagram** the `images` folder. 


# Module 4

## Architecture v4.0

## [Infrastructre Block Diagram ](https://git.hs-coburg.de/ADAPT/adapt_main/src/branch/main/images/infra_architec_module_4.jpg)
![Infrastructre Block Diagram](https://git.hs-coburg.de/ADAPT/adapt_main/raw/branch/main/images/infra_architec_module_4.jpg)

## [Ego-Vehicle Block Diagram ](https://git.hs-coburg.de/ADAPT/adapt_main/raw/branch/main/images/images/ev_architec_module_4.jpg)
![Ego-Vehicle Block Diagram](https://git.hs-coburg.de/ADAPT/adapt_main/raw/branch/main/images/ev_architec_module_4.jpg)

In this module we have updated our system architecture for both the Infrastructure and the EV. We have added parking spot updater and infrastructure’s transceiver to the system architecture of the Infrastructure. Similarly to the EV infrastructure we have shifted the parking spot selector to plan phase of the EV architecture and changed UI1 to vehicle interface and U2 to mobile interface.


## User Stories
![User Stories ](https://git.hs-coburg.de/ADAPT/adapt_main/raw/branch/main/images/user_stories.jpg)

## Component Responsibilities

| Component| Team Members  |
|--------|-------------|
| [Vehicle Interface](https://git.hs-coburg.de/ADAPT/adapt_vi.git) | Ritwik Ranjit |
| [Parking Spot Selector](https://git.hs-coburg.de/ADAPT/adapt_spotsl.git)| Bakar |
| [Route Computer](https://git.hs-coburg.de/ADAPT/adapt_roucomp.git)  | Riddhesh Dalvi |
| [Localization](https://git.hs-coburg.de/ADAPT/adapt_loc.git)  | Ibrahim Al-Dabbagh |
| [Environment Model](https://git.hs-coburg.de/ADAPT/adapt_envmod.git)  | Harsh Patil |
| [Behaviour Planning](https://git.hs-coburg.de/ADAPT/adapt_behplan.git) | Amod Patil & Anish Patil|
| [Lateral and Longitudinal Control](https://git.hs-coburg.de/ADAPT/adapt_latlongcon.git) |Anish Patil |
| [EV Transceiver](https://git.hs-coburg.de/ADAPT/adapt_envmod.git) | Harsh Patil & Anish Patil |
| [Infrastructure Transceiver](https://git.hs-coburg.de/ADAPT/adapt_inf_trans.git)  | Swati Upadhyay |
| [Live Tracker](https://git.hs-coburg.de/ADAPT/adapt_livtrac.git) | Ibrahim Al-Dabbagh |
| [Parking Spot Updater](https://git.hs-coburg.de/ADAPT/adapt_inf_spotupd.git) | Swati Upadhyay |


## Functionalities

### [Vehicle Interface](https://git.hs-coburg.de/ADAPT/adapt_vi)
The Vehicle Interface generates a Graphical Interface for ADAPT. The first frame is the 
introduction to the Adapt system with a "GO" button which takes the user to 2nd frame in 
which the user can type in the Name, Licence plate number and select a checkbox for 
Preference of parking.
### [EV Transceiver](https://git.hs-coburg.de/ADAPT/adapt_transceiver) 
This component is responsible for transmitting CAM, CPM, EVCSN messages and receiving 
data between Ego-vehicle, Infrastructure, and other traffic participants.
### [Infrastructure Transceiver](https://git.hs-coburg.de/ADAPT/adapt_inf_trans)
The infrastructure transceiver is like a translator that changes the parking spot list into an 
EVCSN message. It listens to the parking spot list that's shared under the topic "/spot_list" and 
then translates that information into the EVCSN message.
### [Spot Selector](https://git.hs-coburg.de/ADAPT/adapt_spotsl)
The Parking Spot Selector component works between the Vehicle Interface (VI), the 
infrastructure's (EV CSN) messages, and Route Computer. It receives user-chosen preferences 
from the Vehicle Interface and aggregates EV CSN messages from the infrastructure, which 
contain attributes and locations of available parking spots. Upon receiving this information, 
the Parking Spot Selector sends the selected parking spot location to the Route Computer and 
the Infrastructure, facilitating the booking and navigation process. 
### [Spot Updater](https://git.hs-coburg.de/ADAPT/adapt_inf_spotupd) 
The main function of Spot Updater is to update the list of available parking spot based on the 
input from the object detection and spot selector continuously. Whenever the spot updater 
receives a selected spot from the spot selector by the EV it updates the available parking spots. 
### [Localization](https://git.hs-coburg.de/ADAPT/adapt_loc) 
The localization component provides a precise location of the Ego-Vehicle with respect to its 
environment. It is designed to handle real-time localization data from motion capture systems 
used in the Model City. It processes incoming data from the motion capture system, and 
publishes X, Y, Z positions and orientation (Euler angles). The component leverages 
quaternion to Euler conversion to provide intuitive angle representations.
### [Route Computer](https://git.hs-coburg.de/ADAPT/adapt_roucomp) 
Route computer is a component which determines the process of figuring out the optimum 
route to the selected parking spot. It outputs an effective route for the EV to reach its selected 
parking spot which is further sent to Behaviour Planning. 
### [Live Tracker](https://git.hs-coburg.de/ADAPT/adapt_livtrac)
The LiveTracker component is essential for providing real-time localization and status updates 
for the ego vehicle. It is specifically designed to communicate live positional data and 
notifications directly to a mobile interface, enhancing monitoring and control capabilities. 
### [Environmental Model](https://git.hs-coburg.de/ADAPT/adapt_envmod) 
This component is responsible for the environment perception for the ADAPT. It recieves 
detected objects from LiDAR and detectnet and the vehicle position through Localization 
component and publishes them in the form of OccupancyGrid for the rest of the system. 
### [Behaviour Planning](https://git.hs-coburg.de/ADAPT/adapt_behplan.git)
Behaviour Planning integrates inputs from the Environment Model and Route Computer, 
determining the vehicle's path, speed, and manoeuvres based on the inputs from the 
Environmental Model which gives the occupancy grid map and the Route computer which 
Provides the optimal route towards the parking spot. After computing all the inputs, Behaviour 
Planning outputs speed limits and manoeuvre commands in the form of a Twist message, which 
are executed by the Lateral and Longitudinal Control systems. 
### [Lateral and Longitudinal control](https://git.hs-coburg.de/ADAPT/adapt_latlongcon.git) 
In our system architecture, the vehicle's movement is controlled by the lateral and longitudinal 
component. It takes the speed manoeuvres from the Behaviour planning component and then 
sends the command via CAN BUS to the drive motor.


## Dependencies
Sofware Depenency:

1. [Ubuntu Version : Ubuntu 20.04](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview)
2. [Ros version: Ros2Foxy](https://docs.ros.org/en/foxy/Installation.html)
3. [Mocap msgs](https://github.com/ros-drivers/mocap_optitrack)
4. [V2X msg](https://git.hs-coburg.de/Autonomous_Driving/v2x.git)
5. [ROS2_PCAN](https://git.hs-coburg.de/Autonomous_Driving/ros2_pcan.git)
6. [Ros Deeplearning](https://git.hs-coburg.de/Autonomous_Driving/ros_deep_learning)
7. [Realsense_Camera](https://github.com/IntelRealSense/realsense-ros)
8. [nav2_bringup](https://github.com/open-navigation/navigation2/blob/main/nav2_bringup/README.md)
 
Hardware Depenency:

1. Optitrack Mocap system
2. Intel-Realsense Camera


## Installation Instructions

1. Clone the repository:
```bash
    git clone https://git.hs-coburg.de/ADAPT/adapt_main.git
```
2. Change to the cloned directory:
```bash
    cd adapt_main
```
3. Import the repositories listed in the adapt_repos.repo file:
```bash
    vcs import src < adapt_repos.repo
```
4. Navigate to the root of your ROS 2 workspace:
```bash
    cd ..
```
5. Build the workspace using `colcon`:
```bash
    colcon build --symlink-install
```
## Running Instructions
1. Source the work space before running:
```bash
    source install/setup.bash
```

2. Navigate to the launch folder:
```bash
    cd launch
```
3. Run the launch file with ROS 2:
 - To initiate the ADAPT we run the demo1 launch file where we run the Vehicle interface node, infrastructure tranceiver, parking spot selector nodes
```bash
    ros2 launch demo1.py
```
- To visualize the poses and the oreintations of the EV and the other cars (In order to visualize the poses and the orientation of the cars, make sure they are transmitting CAM messages.)
```bash
    ros2 launch demo2.py
```
- To Drive the EV, do the following:
```bash
    ros2 launch demo3.py
```
Now run the ros2_pcan node
```bash
    ros2 run ros2_pcan ros2pcan_node
```


3. Start RealSense camera:
```bash
ros2 launch realsense2_camera rs_launch.py
```
4. Starting DetectNet:
```bash
    ros2 launch ros_deep_learning detectnet.ros2.launch
```
> :memo: **Note:** Maintainer: **TEAM ADAPT**. 