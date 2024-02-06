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

* **Success Guarantee:** EV parked and locked at the nearest feasible spot.

* **Steps:**  
    1. User exits car & commands vehicle to park; vehicle locks after door closes.
    2. EV initiates communication with infrastructure for parking spot list.
    3. EV receives available spot data from infrastructure.
    4. EV computes nearest feasible parking spots.
    5. EV sends confirmation to infrastructure about the chosen spot.
    6. EV selects best route to the parking spot.
    7. EV drives to and parks at the spot, checking for obstacles.
    8. If spot is inaccessible, EV requests an alternative spot from infrastructure.

# Architecture v2.0
Considering the nature of our project and due to the fact that is dealing with two saparete systems, we had to split our architecture into 2 blocks diagrams, one for the **Infrastructre** and one for **Ego-Vehicle**. These two parts will communicate with each other through **V2X** communication.

## [Infrastructre Block Diagram ](https://git.hs-coburg.de/ADAPT/adapt_main/src/branch/main/images/infra-archi.png)
![Infrastructre Block Diagram](/images/infra-archi.png "Infrastructre")

## [Ego-Vehicle Block Diagram ](https://git.hs-coburg.de/ADAPT/adapt_main/src/branch/main/images/ev-archi.png)
![Ego-Vehicle Block Diagram](/images/ev-archi.png "Ego-Vehicle")

## [Ego-Vehicle RQT](https://git.hs-coburg.de/ADAPT/adapt_main/src/branch/main/images/rqt_full.png)
![Ego-Vehicle RQT](/images/rqt_full.png "Ego-Vehicle")

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

# Components and Functionality:
#### This section will be devided into 3 parts accoring to the Architecture as Sense, Plan, and Act.
## 1. Sense 
### [Parking Spot Selector](https://git.hs-coburg.de/ADAPT/adapt_spotsl)
In our system, the EV receives a list of available parking spot from the infrastructure’s database then the Spot Selection component selects a most suitable parking spot based on predefined user preferences in UI

| **In/Out** | **Topic Name**| **Message Type** | **Description** |
| --------- | ---------- | ---------- | ----------- |
| Input | /infraspot_list|  PoseStamped| Location of parking spots in the surrounding area  |
| Output | /selected_spot_location | PoseStamped | The occupant information for creating an Unique ID | 

> :memo: **Note:** Repository named as **"adapt_sposel"**.  
### [User Interface](https://git.hs-coburg.de/ADAPT/adapt_ui)
USER INTERFACE 1:
The User Interface 1 is the primary interaction of the User with the ADAPT. The User Interface 1 aids the user to input their Information to the system and then give command to park the vehicle, which inturn initializes the system. It is present in the Ego Vehicle.

USER INTERFACE 2:
The User Interface 2 (present on user's hand) aids the User to track the location of the Ego vehicle at all times also it displays the location where the Ego vehicle is going to be parked.

#### UI 1
| In/Out | Topic Name| Message Type | Description | 
| --------- | ------------ | ---------- | ----------- |
| Input | /info_info | string | The occupant_info for creating Unique ID |
| Input | /loc_pose | PoseStamped | The current position of Ego vehicle (EV) |
| Input | /selected_spot_location | PoseStamped| The selected parking spot for the EV.|
| Output | /spot_location | PoseStamped | The location of the selected spot to park.|
| Output | /occupant_info| string | The information of occupant details, selected parking spot and EV location.|

#### UI 2
| In/Out | Topic Name| Message Type | Description | 
| --------- | ---------- | ---------- | ----------- |
| Input | /live_loc| PoseStamped | The location of the EV |
| Output | /display| PoseStamped | The continous tracked location of the EV.|

> :memo: **Note:** Repository named as **"adapt_ui"**.  
### [Localization](https://git.hs-coburg.de/ADAPT/adapt_loc)
The localization component provides a precise location of the Ego-Vehicle with respect to its environment after taking the input data from the perception sensors, the stored Digital Maps and the coordinates from the GNSS. Currently only set up for working with the OptiTrack system in the model city.

#### Component Interfaces
| **In/Out** | **Topic Name**| **Message Type** | **Description** | 
| --------- | ---------- | ---------- | ----------- |
| Input | camera/image_raw | Image | Image data from RealSense camera (not being used for now) | 
| Input | PointCloud2 | LaserScan | LiDar detections (not being used for now) | 
| Input | sensor_msgs/LaserScan | LaserScan | Radar detections (not being used for now)(Will be updated) |
| Input | sensor_msgs/msgs/NavSatFix | PointStamped | Positioning data from GNSS (not being used for now)(Will be updated) |
| Input | Map_data | Static Map | External Maps stored within the system (not being used for now)(Will be updated) |
| Input | /rigid_bodies | RigidBodies | Input from Optitrack System to work in the Model city |
| Output | /loc_pose | PoseStamped | Vehicle Pose |

> :memo: **Note:** Repository named as **"adapt_loc"**.  
### [Lane and Boundary Detection](https://git.hs-coburg.de/ADAPT/adapt_lanboun)
Lane detection is a fundamental component for the perception system of autonomous vehicles. Becuase It provides critical information for navigation, safety,
and overall effective operation in diverse driving conditions. Without accurate and reliable lane detection, the autonomous vehicle may struggle to navigate and respond appropriately to the dynamic and complex nature of real-world traffic scenarios.

| In/Out  | Topic Name                        | Message Type | Description                          |
|---------|-----------------------------------|--------------|--------------------------------------|
| Input   | /camera/image_raw                 | Image        | Image frames from realsense camera    |
| Output  | /lane_detection/lane_info         | LaneInfo  | Detected lane information to Environmental model component     |

> :memo: **Note:** Repository named as **"adapt_lanboun"**.  
### [Object Detection](https://git.hs-coburg.de/ADAPT/adapt_obj)

> :warning: **Important Update:** Currently, We have decided to use the DetectNet Object Detection  in our implementation.

For more information:
- Basic Info on object detection: https://github.com/dusty-nv/jetson-inference
- ROS node for jetson_inference: https://github.com/dusty-nv/ros_deep_learning

The object detection algorithms use visual data such as images, videos, and laser scan points to analyze and identify objects' locations. Identifying and understanding the surrounding environment is essential for safe vehicle navigation and parking. As a result, the information produced by the object detection process is provided to the Environment model.

| In/Out | Topic Name| Message Type | Description | 
| --------- | ---------- | ---------- | ----------- |
| Input | /Raw images|  image_in| Raw input image | |
| Output | /Detection| vision_msgs/Detection2DArray  | Detection results (Bounding boxes, class IDs, confidences) |


> :memo: **Note:** Repository named as **"adapt_obj"**. 
### [Infrastructre](https://git.hs-coburg.de/ADAPT/adapt_inf)


| In/Out | Topic Name| Message Type | Description | 
| --------- | ---------- | ---------- | ----------- |
| Input | N/A|  | N/A |N/A |
| Input |N/A | |N/A |N/A |
| Output | N/A |  N/A| N/A | 

> :memo: **Note:** Repository named as **"adapt_inf"**.

## 2. Plan 
### [Behaviour Planning](https://git.hs-coburg.de/ADAPT/adapt_bahplan) 
Behaviour Planning integrates inputs from the Environmental Model and Route Computer, determining the vehicle's path, speed, and maneuvers based on surrounding conditions. It outputs waypoints, speed limits, and maneuver commands, which are executed by the Lateral and Longitudinal Control systems.

| In/Out | Topic Name| Message Type | Description | 
| --------- | ---------- | ---------- | ----------- |
| Input | /route|  nav_msgs/msg/Path| A optimum route from the vehicle's location to the parking spot | |
| Input |/complete_model | OcupancyGrid |Complete model of where the vehicle is located with respect to its environment | |
| Output | /beh_spd | v2x/Speed | Speed specifications of the vehicle | 
| Output | /beh_mcmd |  v2x/LateralAcceleration | Acceleration to the lateral direction |

> :memo: **Note:** Repository named as **"adapt_behplan"**.  
### [Live Tracker](https://git.hs-coburg.de/ADAPT/adapt_livtrac)
The component takes data from localization component and sends the live location to the user interfaces

| In/Out | Topic Name| Message Type | Description | 
| --------- | ---------- | ---------- | ----------- |
| Input | /vehicle_location| PoseStamped | The location of the EV att all time from the localisation unit. |
| Output | /live_loc| PoseStamped| The live location of the EV during its parking manoeuver. |

> :memo: **Note:** Repository named as **"adapt_livtrac"**.  
### [Environmental Model](https://git.hs-coburg.de/ADAPT/adapt_envmod)
The Environmental Model is a critical component in the architecture of autonomous vehicles, serving as the system's eyes and understanding of the external world. This model collects and processes data from a suite of other components enabling the vehicle to understand and react to its environment effectively.

| In/Out | Topic Name| Message Type | Description | 
| --------- | ---------- | ---------- | ----------- |
| Input | /detectnet/detections| Detection2DArray | The detectnet detections |
| Input | /loc_pose| PoseStamped | The current position of our vehicle |
| Input  | /lane_detection/lane_info         | LaneInfo | Detected lane information to Environmental model component     |
| Output | /complete_model| OcupancyGrid | Complete model of where the vehicle is located with respect to its environment|

> :memo: **Note:** Repository named as **"adapt_envmod"**.  
### [Route Computer](https://git.hs-coburg.de/ADAPT/adapt_roucomp)
Route computer is the process of figuring out the optimum route for the vehicle to take from where it is to the parking spot that has been selected. The planning of a safe and effective route for the car to reach its destination makes this an essential part of the total autonomous parking system. 

| In/Out | Topic Name| Message Type | Description | 
| --------- | ---------- | ---------- | ----------- |
| Input | /loc_pose | PoseStamped | The current position of our vehicle |
| Input | /spot_location | PoseStamped | The selected parking spot's location from UI |
| Input | /map_data | OccupancyGrid | The local map data from localization |
| Output | /route | PoseArray | A optimum route from the vehicle's location to the parking spot|

> :memo: **Note:** Repository named as **"adapt_roucomp"**. 

## 3. Act 
### [Lateral and Longitude Control](https://git.hs-coburg.de/ADAPT/adapt_latlongcon)
The lateral and longitudinal control refers to steering and speed management: lateral control governs side-to-side steering for lane positioning, while longitudinal control manages forward and backward motion, including acceleration and deceleration.

| In/Out | Topic Name| Message Type | Description | 
| --------- | ---------- | ---------- | ----------- |
| Input | /beh_spd | v2x/Speed | Speed specifications of the vehicle | 
| Input | /beh_mcmd |  v2x/LateralAcceleration | Acceleration to the lateral direction |
| Output | /cmd_vel | geometry_msgs/Twist | Linear and angular velocity command |

> :memo: **Note:** Repository named as **"adapt_latlongcon"**. 

### [Transmitter](https://git.hs-coburg.de/ADAPT/adapt_trnsmtr)
The transmitter is responsible for sending and receiving messages from the EV to Infrastructure and vice versa.


| In/Out | Topic Name| Message Type | Description | 
| --------- | ---------- | ---------- | ----------- |
| Input | /occupant_info| String |The details of the user.|
| Input | /loc_pose| PoseStamped | The initial location of the EV.|
| Input | /detectnet/detctions| Detection2DArray | The objection detection list to Infrastructure |
| Input | /selected_spot_location| PoseStamped | The objection detection list to Infrastructure |
| Output | /ev_location| PoseStamped | The initial location of the EV|
| Output | /selected_spot| PoseStamped | The selected parking location.|
| Output | /user_info| String  | The details of the user.|
| Output | /cam_data | |It is responsible for publishing the CAM messages for V2X application|
| Output | /cpm_data | |It is responsible for publishing the CPM messages for V2X application|

> :memo: **Note:** Repository named as **"adapt_transmitter"**. 

### [Parking spot updater](https://git.hs-coburg.de/ADAPT/adapt_spotupd)
Parking spot updater updates the parking spot list in the Infrastructure data base. It takes inputs from object detection which is objects in and around the parking spot and the Occupant information. The Output is then given to the Infrastructure Data base which updates the parking spot list.

| In/Out | Topic Name| Message Type | Description | 
| --------- | ---------- | ---------- | ----------- |
| Input | /occupant_info|  | The occupant_info for creating Unique ID | |
| Input |/object_list | |objects in and around the parking spot | |
| Output | /updated_list |  | Updated parking spot List | 

> :memo: **Note:** Repository named as **"adapt_spotupd"**.



### [Custom Messages](https://git.hs-coburg.de/ADAPT/adapt_msgs)
This repository has been created to gather all of our custom messages in one package (See Repository for more details).
The number of messages in this repository well change depending on the need of a custom message.

| Topic Name| Message Type | Description | 
| ---------- | ---------- | ----------- |
| /lane_detection/lane_info | LaneInfo |Detected lane information |
| /act_cmd | CarCom | actuator commands |
| N/A |  N/A| N/A | 

> :memo: **Note:** Repository named as **"adapt_msgs"**.


# Task and Component Allocation
The following table shows task and component allocation between team members based on the Repository:


|  Name | Repository Name | Maintainer |
|----------------|-----------------|------------|
| Main | [**adapt_main**](https://git.hs-coburg.de/ADAPT/adapt_main) | Ibrahim Al Dabbagh, Harshawardhan Patil |
| Behaviour Planning | [adapt_behplan](https://git.hs-coburg.de/ADAPT/adapt_bahplan) | Amod Patil |
| Environmental Model | [adapt_envmod](https://git.hs-coburg.de/ADAPT/adapt_envmod) | Harshawardhan Patil |
| Infrastructure Simulator | [adapt_inf](https://git.hs-coburg.de/ADAPT/adapt_inf) | Swati Upadhyay |
| Lane and Boundary Detection | [adapt_lanboun](https://git.hs-coburg.de/ADAPT/adapt_lanboun.git) | Ibrahim Al Dabbagh |
| Lateral and Longitude Control | [adapt_latlongcon](https://git.hs-coburg.de/ADAPT/adapt_latlongcon) | Anish Patil |
| Live Tracker | [adapt_livtrac](https://git.hs-coburg.de/ADAPT/adapt_livtrac) | Ritwik Ranjit, Amod Patil, Riddhesh Dalvi |
| Localization | [adapt_loc](https://git.hs-coburg.de/ADAPT/adapt_loc) | Srijan Gupta |
| Custom Messages | [adapt_msgs](https://git.hs-coburg.de/ADAPT/adapt_msgs) | Ibrahim Al Dabbagh, Anish Patil |
| Object Detection | [adapt_obj](https://git.hs-coburg.de/ADAPT/adapt_obj) | Ibrahim Al Dabbagh, Harshawardhan Patil |
| Parking Spot Compatibility and Availability Checker | [adapt_psc_ac](https://git.hs-coburg.de/ADAPT/adapt_psc_ac) | Harshawardhan Patil |
| Route Computer | [adapt_roucomp](https://git.hs-coburg.de/ADAPT/adapt_roucomp) | Riddhesh Dalvi |
| Parking Spot Selector | [adapt_spotsl](https://git.hs-coburg.de/ADAPT/adapt_spotsl) | Ritwik Ranjit, Riddhesh Dalvi, Amod Patil |
| Parking Spot Updater | [adapt_spotupd](https://git.hs-coburg.de/ADAPT/adapt_spotupd) | Amod Patil |
| Transmitter | [adapt_transmitter](https://git.hs-coburg.de/ADAPT/adapt_trnsmtr) | Ritwik Ranjit, Anish Patil, Harshawardhan Patil |
| User Interface | [adapt_ui](https://git.hs-coburg.de/ADAPT/adapt_ui) | Ritwik Ranjit |

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
6. Source the work space before running:
```bash
    source install/setup.bash
```
7. Run the launch file with ROS 2:
```bash
    ros2 launch adapt_launch.py
```
