# ADAPT OVERVIEW
#### Welcome to the main repository of **ADAPT** System. This repository will help you navigate through our orgnization repositories and hopefully provide a comprehensive understanding of the system architecture and breifly describe components functionality.

# Architecture v2.0
For a better understanding, we have split our architecture into 2 blocks diagrams, one for the **Infrastructre** and one for **Ego-Vehicle**. These two parts will communicate with each other through **V2X** communication.

## Infrastructre Block Diagram

![Infrastructre Block Diagram](/images/infra-archi.png "Infrastructre")

## Ego-Vehicle Block Diagram

![Ego-Vehicle Block Diagram](/images/ev-archi.png "Ego-Vehicle")

# Components and Functionality:


## [Lateral and Longitude Control](https://git.hs-coburg.de/ADAPT/adapt_latlongcon)
The lateral and longitudinal control refers to steering and speed management: lateral control governs side-to-side steering for lane positioning, while longitudinal control manages forward and backward motion, including acceleration and deceleration.

| In/Out | Topic Name| Message Type | Description | 
| --------- | ---------- | ---------- | ----------- |
| Input | /beh_spd | v2x/Speed | Speed specifications of the vehicle | 
| Input | /beh_mcmd |  v2x/LateralAcceleration | Acceleration to the lateral direction |
| Output | /cmd_vel | geometry_msgs/Twist | Linear and angular velocity command |

> :memo: **Note:** Repository named as **"adapt_latlongcon"**. 
## [Behaviour Planning](https://git.hs-coburg.de/ADAPT/adapt_bahplan) 
Behaviour Planning integrates inputs from the Environmental Model and Route Computer, determining the vehicle's path, speed, and maneuvers based on surrounding conditions. It outputs waypoints, speed limits, and maneuver commands, which are executed by the Lateral and Longitudinal Control systems.

| In/Out | Topic Name| Message Type | Description | 
| --------- | ---------- | ---------- | ----------- |
| Input | /route|  nav_msgs/msg/Path| A optimum route from the vehicle's location to the parking spot | |
| Input |/complete_model | |Complete model of where the vehicle is located with respect to its environment | |
| Output | /beh_spd | v2x/Speed | Speed specifications of the vehicle | 
| Output | /beh_mcmd |  v2x/LateralAcceleration | Acceleration to the lateral direction |

> :memo: **Note:** Repository named as **"adapt_behplan"**.  
## [Live Tracker](https://git.hs-coburg.de/ADAPT/adapt_livtrac)
The component takes data from localization component and sends the live location to the user interfaces

| In/Out | Topic Name| Message Type | Description | 
| --------- | ---------- | ---------- | ----------- |
| Input | /vehicle_location| geometry_msgs/Pose | The location of the EV att all time from the localisation unit. |
| Output | /live_loc| geometry_msgs/Pose| The live location of the EV during its parking manoeuver. |

> :memo: **Note:** Repository named as **"adapt_livtrac"**.  
## [Environmental Model](https://git.hs-coburg.de/ADAPT/adapt_envmod)
The Environmental Model is a critical component in the architecture of autonomous vehicles, serving as the system's eyes and understanding of the external world. This model collects and processes data from a suite of other components enabling the vehicle to understand and react to its environment effectively.

| In/Out | Topic Name| Message Type | Description | 
| --------- | ---------- | ---------- | ----------- |
| Input | /detectnet/detections| Detection2DArray | The detectnet detections |
| Input | /loc_pose| Pose | The current position of our vehicle |
| Input  | /lane_detection/lane_info         | Float64MultiArray  | Detected lane information to Environmental model component     |
| Output | /complete_model| | Complete model of where the vehicle is located with respect to its environment|

> :memo: **Note:** Repository named as **"adapt_envmod"**.  
## [Route Computer](https://git.hs-coburg.de/ADAPT/adapt_roucomp)
Route computer is the process of figuring out the optimum route for the vehicle to take from where it is to the parking spot that has been selected. The planning of a safe and effective route for the car to reach its destination makes this an essential part of the total autonomous parking system. 

| In/Out | Topic Name| Message Type | Description | 
| --------- | ---------- | ---------- | ----------- |
| Input | /vehicle_location | geometry_msgs/Pose | The current position of our vehicle |
| Input | /spot_location | v2x/msg/evcsn-ts101556-1/ItsChargingStationData | The selected parking spot's location from UI |
| Input | /map_data | v2x/msg/MapData | The local map data from localization |
| Output | /route | nav_msgs/msg/Path | A optimum route from the vehicle's location to the parking spot|

> :memo: **Note:** Repository named as **"adapt_roucomp"**.  
## [Parking Spot Selector](https://git.hs-coburg.de/ADAPT/adapt_sposel)
In our system, the EV receives a list of available parking spot from the infrastructure’s database then the Spot Selection component selects a most suitable parking spot based on predefined user preferences in UI

| **In/Out** | **Topic Name**| **Message Type** | **Description** |
| --------- | ---------- | ---------- | ----------- |
| Input | /parking spots|  evcsn-ts101556-1/ItsChargingStationData| Location of parking spots in the surrounding area  |
| Output | /occupant_info | | The occupant information for creating an Unique ID | 

> :memo: **Note:** Repository named as **"adapt_sposel"**.  
## [User Interface](https://git.hs-coburg.de/ADAPT/adapt_ui)
USER INTERFACE 1:
The User Interface 1 is the primary interaction of the User with the ADAPT. The User Interface 1 aids the user to input their Information to the system and then give command to park the vehicle, which inturn initializes the system. It is present in the Ego Vehicle.

USER INTERFACE 2:
The User Interface 2 (present on user's hand) aids the User to track the location of the Ego vehicle at all times also it displays the location where the Ego vehicle is going to be parked.

## UI 1
| In/Out | Topic Name| Message Type | Description | 
| --------- | ---------- | ---------- | ----------- |
| Input | /info_info | string | The occupant_info for creating Unique ID |
| Input | /loc_pose | geometry_msgs/Pose | The current position of Ego vehicle (EV) |
| Input | /selected_spot_location | v2x/msg/evcsn-ts101556-1/ItsChargingStationData | The selected parking spot for the EV.|
| Output | /spot_location | v2x/msg/evcsn-ts101556-1/ItsChargingStationData | The location of the selected spot to park.|
| Output | /occupant_info| string | The information of occupant details, selected parking spot and EV location.|

## UI 2
| In/Out | Topic Name| Message Type | Description | 
| --------- | ---------- | ---------- | ----------- |
| Input | /live_loc| geometry_msgs/Pose | The location of the EV |
| Output | /display| geometry_msgs/Pose | The continous tracked location of the EV.|

> :memo: **Note:** Repository named as **"adapt_ui"**.  
## [Localization](https://git.hs-coburg.de/ADAPT/adapt_loc)
The localization component provides a precise location of the Ego-Vehicle with respect to its environment after taking the input data from the perception sensors, the stored Digital Maps and the coordinates from the GNSS. Currently only set up for working with the OptiTrack system in the model city.

## Component Interfaces
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
## [Lane and Boundary Detection](https://git.hs-coburg.de/ADAPT/adapt_lanboun)
Lane detection is a fundamental component for the perception system of autonomous vehicles. Becuase It provides critical information for navigation, safety,
and overall effective operation in diverse driving conditions. Without accurate and reliable lane detection, the autonomous vehicle may struggle to navigate and respond appropriately to the dynamic and complex nature of real-world traffic scenarios.

| In/Out  | Topic Name                        | Message Type | Description                          |
|---------|-----------------------------------|--------------|--------------------------------------|
| Input   | /camera/image_raw                 | Image        | Image frames from realsense camera    |
| Output  | /lane_detection/lane_info         | LaneInfo  | Detected lane information to Environmental model component     |

> :memo: **Note:** Repository named as **"adapt_lanboun"**.  
## [Object Detection](https://git.hs-coburg.de/ADAPT/adapt_obj)
The object detection algorithms use visual data such as images, videos, and laser scan points to analyze and identify objects' locations. Identifying and understanding the surrounding environment is essential for safe vehicle navigation and parking. As a result, the information produced by the object detection process is provided to the Environment model.

| In/Out | Topic Name| Message Type | Description | 
| --------- | ---------- | ---------- | ----------- |
| Input | /Raw images|  image_in| Raw input image | |
| Output | /Detection| vision_msgs/Detection2DArray  | Detection results (Bounding boxes, class IDs, confidences) |

> :memo: **Note:** Repository named as **"adapt_obj"**. 
## [Transmitter](https://git.hs-coburg.de/ADAPT/adapt_trnsmtr)
The transmitter is responsible for sending and receiving messages from the EV to Infrastructure and vice versa.


| In/Out | Topic Name| Message Type | Description | 
| --------- | ---------- | ---------- | ----------- |
| Input | /occupant_info| |The information of occupant details, selected parking spot and vehicle location  |
| Input | /vehicle_location| geometry_msgs/Pose | The current location of the EV.|
| Input | /Detection| vision_msgs/Detection2DArray | The objection detection list to Infrastructure |
| Input | /lane_detection/lane_info | String | Detected lane information to environmental model Component|
| Output | /data_list|  | The information of occupant details, selected parking spot and vehicle location|
| Output | /cam_data | |It is responsible for publishing the CAM messages for V2X application|
| Output | /cpm_data | |It is responsible for publishing the CPM messages for V2X application|

> :memo: **Note:** Repository named as **"adapt_transmitter"**. 
## [Parking spot compatibility and availibility checker](https://git.hs-coburg.de/ADAPT/adapt_psc_ac)

> :memo: **Note:** Repository named as **"adapt_psc_ac"**.
## [Parking spot updater](https://git.hs-coburg.de/ADAPT/adapt_spotupd)
Parking spot updater updates the parking spot list in the Infrastructure data base. It takes inputs from object detection which is objects in and around the parking spot and the Occupant information. The Output is then given to the Infrastructure Data base which updates the parking spot list.

| In/Out | Topic Name| Message Type | Description | 
| --------- | ---------- | ---------- | ----------- |
| Input | /occupant_info|  | The occupant_info for creating Unique ID | |
| Input |/object_list | |objects in and around the parking spot | |
| Output | /updated_list |  | Updated parking spot List | 

> :memo: **Note:** Repository named as **"adapt_spotupd"**.
## Initial setup
```bash
cd adapt_main
vcs import src < adapt_repos.repo
