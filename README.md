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

# Architecture v3.0
Considering the nature of our project and due to the fact that is dealing with two saparete systems, we had to split our architecture into 2 blocks diagrams, one for the **Infrastructre** and one for **Ego-Vehicle**. These two parts will communicate with each other through **V2X** communication.

## [Infrastructre Block Diagram ](https://git.hs-coburg.de/ADAPT/adapt_main/src/branch/main/images/archi_v3_2.jpg)
![Infrastructre Block Diagram](https://git.hs-coburg.de/ADAPT/adapt_main/raw/branch/main/images/archi_v3_2.jpg)

## [Ego-Vehicle Block Diagram ](https://git.hs-coburg.de/ADAPT/adapt_main/raw/branch/main/images/Team%20Green%20-%20ADAPT.png)
![Ego-Vehicle Block Diagram](https://git.hs-coburg.de/ADAPT/adapt_main/raw/branch/main/images/ego-veihcle-v3.png)

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
# Ego Vehicle
#### This section will be devided into 3 parts accoring to the Architecture as Sense, Plan, and Act.
## 1. Sense 

### [User Interface](https://git.hs-coburg.de/ADAPT/adapt_ui)
Vehicle Interface :
The User Interface 1 is the primary interaction of the User with the ADAPT. The User Interface 1 aids the user to input their Information to the system and then give command to park the vehicle, which inturn initializes the system. It is present in the Ego Vehicle.

Mobile Interface:
The User Interface 2 (present on user's hand) aids the User to track the location of the Ego vehicle at all times also it displays the location where the Ego vehicle is going to be parked.

#### Vehicle Interface
| In/Out | Topic Name| Message Type | Description | 
| --------- | ------------ | ---------- | ----------- |
| Input | /info_info | string | The occupant_info for creating Unique ID |
| Input | /loc_pose | PoseStamped | The current position of Ego vehicle (EV) |
| Input | /selected_spot_location | PoseStamped| The selected parking spot for the EV.|
| Output | /spot_location | PoseStamped | The location of the selected spot to park.|
| Output | /occupant_info| string | The information of occupant details, selected parking spot and EV location.|

#### Mobile Interface
* Key Features
1. **Real-Time Location Tracking**: The interface displays a live map (Model City) showing the current location of the Ego vehicle. This feature enable users to monitor the vehicle’s movement and ensure it reaches the intended destination safely.
2. **Vehicle Status Indication**: Users can see at a glance whether the vehicle is parked or still in motion. This information is presented through a toggle switch that shows 'Moving' or 'Parked', providing immediate understanding of the vehicle's state.
3. **Parking Preferences**: The app allows users to view their chosen parking preferences. Options include paid electronic charging parking spots, free parking areas, or any available spot. 

> :memo: **Note:** Repository named as **"adapt_mi"**.  


### [Localization](https://git.hs-coburg.de/ADAPT/adapt_loc)

The localization component provides a precise location of the Ego-Vehicle with respect to its environment. It is designed to handle real-time localization data from motion capture systems used in the Model City. It processes incoming data from the motion capture system, and publishes X, Y, Z positions and orientation (Euler angles). The component leverages quaternion to Euler conversion to provide intuitive angle representations.

| In/Out | Topic Name          | Message Type                 | Description                                  |
|--------|---------------------|------------------------------|----------------------------------------------|
| Input  | `/pose_modelcars`     | `mocap_msgs/msg/RigidBodies` | Receives data from motion capture systems.   |
| Output | `/loc_pose`         | `geometry_msgs/msg/PoseStamped` | Publishes processed pose information.     |
| Output | `/eular_angels`         | `geometry_msgs/msg/Vector3` | Publishes Euler angles representing orientation.     |

> :memo: **Note:** Repository named as **"adapt_loc"**. 


### [Object Detection](https://git.hs-coburg.de/ADAPT/adapt_obj)

Our DetectNet model has been trained to recognize several classes of objects which are integral to the autonomous driving context. These classes, annotated in the dataset, include:

- **Person**: Individuals dummies in the model city.
- **traffic_light**: Signalling devices positioned at road intersections, pedestrian crossings, and other locations to control flows of traffic.
- **potted plant**: Trees, shrubs, and other plant within the model city.
- **car**: Cars, trucks, and other modes of transportation moving or stationary within the model city.

Each class has been annotated with a unique color code for visual differentiation in the detection process.

#### ROS2 Topics for Object Detection

| In/Out | Topic Name| Message Type | Description | 
| --------- | ---------- | ---------- | ----------- |
| Input | /raw_images|  image_in | Raw input image | |
| Output | /detectnet/detections | vision_msgs/Detection2DArray  | Detection results (Bounding boxes, class IDs, confidences) |

> :memo: **Note:** Repository named as **"adapt_obj"**. 


## 2. Plan 


### [Parking Spot Selector](https://git.hs-coburg.de/ADAPT/adapt_spotsl)
In our system, the EV receives a list of available parking spot from the infrastructure’s database then the Spot Selection component selects a most suitable parking spot based on predefined user preferences in UI

| **In/Out** | **Topic Name**| **Message Type** | **Description** |
| --------- | ---------- | ---------- | ----------- |
| Input | /vi_data |  String | receives user preferences for parking spots, specifically whether they prefer free or paid parking  |
| Input | /evcsn_msg|  ItsEVCSNData | receives data about available parking spots, including details about location and price  |
| Output | /selected_spot | PoseStamped | publishes the location of the parking spot selected based on the user's preference and spot availability | 

> :memo: **Note:** Repository named as **"adapt_sposel"**.  


### [Behaviour Planning](https://git.hs-coburg.de/ADAPT/adapt_bahplan) 
Behaviour Planning integrates inputs from the Environmental Model and Route Computer, determining the vehicle's path, speed, and maneuvers based on surrounding conditions. It outputs waypoints, speed limits, and maneuver commands, which are executed by the Lateral and Longitudinal Control systems.

| In/Out | Topic Name| Message Type | Description | 
| --------- | ---------- | ---------- | ----------- |
| Input | /route|  nav_msgs/msg/Path| A optimum route from the vehicle's location to the parking spot | |
| Input | /complete_model | OccupancyGrid| Complete model of where the vehicle is located with respect to its environment | |
| Input | /loc_pose | PoseStamped|Location of Ego Vehicle | |
| Output | /cmd_vel | geometry_msgs/Twist | linear and angular velocities of the vehicle |

> :memo: **Note:** Repository named as **"adapt_behplan"**.  


### [Live Tracker](https://git.hs-coburg.de/ADAPT/adapt_livtrac)
The Live Tracker component is provides real-time localization and status updates of the ego vehicle. It is specifically designed to communicate live positional data and notifications directly to a mobile interface, enhancing monitoring and control capabilities.


| In/Out | Topic Name            | Message Type               | Description                                            |
|--------|-----------------------|----------------------------|--------------------------------------------------------|
| Input  | `/loc_pose`           | `geometry_msgs/msg/PoseStamped` | Receives current pose updates from vehicle's localization system. |
| Input  | `/route`              | `geometry_msgs/msg/PoseArray`   | Receives predefined route data for navigation guidance. |
| Output | `/live_loc`           | `adapt_msgs/msg/LiveTrack`      | Publishes live tracking information including vehicle's positional and status data. |

> :memo: **Note:** Repository named as **"adapt_livtrac"**.  


### [Environment Model](https://git.hs-coburg.de/ADAPT/adapt_envmod)
This component is for the environment perception for the ADAPT System. It recieves detected objects from LiDAR and detectnet and the vehicle position through Localization component and publishes them in form of OccupancyGrid for the rest of the system.

| In/Out | Topic Name| Message Type | Description | 
| --------- | ---------- | ---------- | ----------- |
| Input | /detectnet/detections| Detection2DArray | The detectnet detections |
| Input | /loc_pose| PoseStamped | The current position of our vehicle |
| Input  | /dolly/LaserScan       | Scan | Detected objecte distance measurements for Environment model component     |
| Output | /complete_model| OcupancyGrid | Complete model of where the vehicle is located with respect to its environment|

> :memo: **Note:** Repository named as **"adapt_envmod"**.  


### [Route Computer](https://git.hs-coburg.de/ADAPT/adapt_roucomp)
Route computer is a component which determines the process of figuring out the optimum route to the selected parking spot. It outputs an effective route for the EV to reach its selected parking spot which is further sent to Behaviour Planning.

Note: For this module Route Computer is generating a straight path for the EV in the form of waypoints according to the model city.
| In/Out | Topic Name| Message Type | Description | 
| --------- | ---------- | ---------- | ----------- |
| Input | /loc_pose | PoseStamped | The current position of our vehicle |
| Input | /spot_location | PoseStamped | The selected parking spot's location from UI |
| Output | /route | PoseArray | A optimum route from the vehicle's location to the parking spot|

> :memo: **Note:** Repository named as **"adapt_roucomp"**. 


## 3. Act 
### [Lateral and Longitude Control](https://git.hs-coburg.de/ADAPT/adapt_latlongcon)
The lateral and longitudinal control refers to steering and speed management: lateral control governs side-to-side steering for lane positioning, while longitudinal control manages forward and backward motion, including acceleration and deceleration.

| In/Out | Topic Name| Message Type | Description | 
| --------- | ---------- | ---------- | ----------- | 
| Input | /cmd_vel |  geometry_msgs/Twist | speed specifications |
| Output | /act_cmd | adapt_msgs/CarCom | actuator commands to steer and accelerate the vehicle |

> :memo: **Note:** Repository named as **"adapt_latlongcon"**. 

### [Transceiver](https://git.hs-coburg.de/ADAPT/adapt_transceiver)
The transceiver is responsible for sending and receiving messages from the EV to Infrastructure and vice versa.


| In/Out | Topic Name| Message Type | Description | 
| --------- | ---------- | ---------- | ----------- |
| Input | /loc_pose| PoseStamped | The location of the EV.|
| Input | /detectnet/detctions| Detection2DArray | The objection detection list to Infrastructure |
| Output | /ev_location| VehData | The converted CAM messages from other vehicles for environment model|
| Output | /cam_msgs | CAM |It is responsible for publishing the CAM messages for V2X application|
| Output | /detected_objects | CPM |It is responsible for publishing the CPM messages for V2X application|

> :memo: **Note:** Repository named as **"adapt_transceiver"**. 

# Infrastructre
#### This section will be devided into 3 parts accoring to the Architecture as Sense, Plan, and Act.
## 1. Sense 

### [parking spot detection for infrastructure](https://git.hs-coburg.de/ADAPT/adapt_inf_od)
This component outlines how parking spots are autonomously selected, communicated to the User Interface (UI), transmitted to the infrastructure, and updated for vehicle access. By understanding these processes, stakeholders gain insight into our system's functionality and architecture.

| In/Out  | Topic Name                        | Message Type | Description                          |
|---------|-----------------------------------|--------------|--------------------------------------|
| Input   | /selected_spot            | PoseStamped    | This message will give us the spot selected by the spot selector  |
| Input | /ev_location        | PoseStamped| This message will give us the location of th ego vehicle    |
| Input   | /user_info            | string   | This message will give us the info of the user |
| Output  | /updated_parking_spots        | ItsChargingStationData| This message will give us the NEW list of updated parking list     |


> :memo: **Note:** Repository named as **"adapt_inf_od"**.


## 2. Plan
### [Parking spot updater](https://git.hs-coburg.de/ADAPT/adapt_inf_spotupd)
Parking spot updater updates the parking spot list in the Infrastructure data base. It takes inputs from object detection which is objects in and around the parking spot and the Occupant information. The Output is then given to the Infrastructure Data base which updates the parking spot list.

| In/Out | Topic Name| Message Type | Description | 
| --------- | ---------- | ---------- | ----------- |
| Input | /occupant_info|  | The occupant_info for creating Unique ID | |
| Input |/object_list | |objects in and around the parking spot | |
| Output | /updated_list |  | Updated parking spot List | 

> :memo: **Note:** Repository named as **"adapt_inf_spotupd"**.

## 3. Act
### [Infrastructure Transceiver](https://git.hs-coburg.de/ADAPT/adapt_inf_transceiver)
...........

| In/Out | Topic Name| Message Type | Description | 
| --------- | ---------- | ---------- | ----------- |
| Input | /occupant_info|  | The occupant_info for creating Unique ID | |
| Input |/object_list | |objects in and around the parking spot | |
| Output | /updated_list |  | Updated parking spot List | 

> :memo: **Note:** Repository named as **"adapt_inf_transceiver"**.

### Custom Messages
### [adapt Messages](https://git.hs-coburg.de/ADAPT/adapt_msgs)
This repository has been created to gather all of our custom messages in one package (See Repository for more details).
The number of messages in this repository well change depending on the need of a custom message.

| Topic Name| Message Type | Description | 
| ---------- | ---------- | ----------- |
| /ev_location | VehData |The converted CAM messages from other vehicles for environment model |
| /act_cmd | CarCom | actuator commands | 
| /live_loc | LiveTrack | The custom message contain the pose of the EV and current status (Parked, Moving) | 
> :memo: **Note:** Repository named as **"adapt_msgs"**.

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
2. Run the launch file with ROS 2:
```bash
    ros2 launch adapt_launch.py
```
3. Start RealSense camera:
```bash
ros2 launch realsense_examples rs_camera.launch.py
```
4. Starting DetectNet:
```bash
    ros2 launch ros_deep_learning detectnet.ros2.launch
```
> :memo: **Note:** Maintainer: **Ibrahim Al Dabbagh**. 