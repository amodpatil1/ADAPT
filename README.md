# ADAPT OVERVIEW
#### Welcome to the main repository of **ADAPT** System. This repository will help you navigate through our orgnization repositories and hopefully provide a comprehensive understanding of the system architecture and breifly describe components functionality.

# Architecture v1.0
For a better understanding, we have splited our architecture into 2 blocks diagrams, one for the **Infrastructre** and one for **Ego-Vehicle**. These two parts will communicate with each other through **V2X** communication.

## Infrastructre Block Diagram

![Infrastructre Block Diagram](/images/infra_architecture.jpg "Infrastructre")

## Ego-Vehicle Block Diagram

![Ego-Vehicle Block Diagram](/images/av_architecture.jpg "Ego-Vehicle")

# Components and Functionality:


## [Lateral and Longitude Control](https://git.hs-coburg.de/ADAPT/adapt_latlongcon)
The lateral and longitudinal control refers to steering and speed management: lateral control governs side-to-side steering for lane positioning, while longitudinal control manages forward and backward motion, including acceleration and deceleration.
> :memo: **Note:** Repository named as **"adapt_latlongcon"**. 
## [Behaviour Planning](https://git.hs-coburg.de/ADAPT/adapt_bahplan) 
Behaviour Planning integrates inputs from the Environmental Model and Route Computer, determining the vehicle's path, speed, and maneuvers based on surrounding conditions. It outputs waypoints, speed limits, and maneuver commands, which are executed by the Lateral and Longitudinal Control systems.
> :memo: **Note:** Repository named as **"adapt_behplan"**.  
## [Live Tracker](https://git.hs-coburg.de/ADAPT/adapt_livtrac)
The component takes data from localization component and sends the live location to the user interfaces
> :memo: **Note:** Repository named as **"adapt_livtrac"**.  
## [Environmental Model](https://git.hs-coburg.de/ADAPT/adapt_envmod)
The Environmental Model is a critical component in the architecture of autonomous vehicles, serving as the system's eyes and understanding of the external world. This model collects and processes data from a suite of other components enabling the vehicle to understand and react to its environment effectively.
> :memo: **Note:** Repository named as **"adapt_envmod"**.  
## [Route Computer](https://git.hs-coburg.de/ADAPT/adapt_roucomp)
Route computer is the process of figuring out the optimum route for the vehicle to take from where it is to the parking spot that has been selected. The planning of a safe and effective route for the car to reach its destination makes this an essential part of the total autonomous parking system. 
> :memo: **Note:** Repository named as **"adapt_roucomp"**.  
## [Parking Spot Selector](https://git.hs-coburg.de/ADAPT/adapt_sposel)
In our system, the EV receives a list of available parking spot from the infrastructure’s database then the Spot Selection component selects a most suitable parking spot based on predefined user preferences in UI
> :memo: **Note:** Repository named as **"adapt_sposel"**.  
## [User Interface](https://git.hs-coburg.de/ADAPT/adapt_ui)
After the User arrives at the destination and commands the system to park the vehicle using the User Interface of the Ego Vehicle depending on the preferences (Shortest route, Fastest route..etc). The User Interface receives the input from the User and localization component to provide the output to transmitter for sharing the information with the Infrastructure.
> :memo: **Note:** Repository named as **"adapt_ui"**.  
## [Localization](https://git.hs-coburg.de/ADAPT/adapt_loc)
The localization component provides a precise location of the Ego-Vehicle with respect to its environment after taking the input data from the perception sensors, the stored Digital Maps and the coordinates from the GNSS.
> :memo: **Note:** Repository named as **"adapt_loc"**.  
## [Lane and Boundary Detection](https://git.hs-coburg.de/ADAPT/adapt_lanboun)
Lane detection is a fundamental component for the perception system of autonomous vehicles. Becuase It provides critical information for navigation, safety,
and overall effective operation in diverse driving conditions. Without accurate and reliable lane detection, the autonomous vehicle may struggle to navigate and respond appropriately to the dynamic and complex nature of real-world traffic scenarios.
> :memo: **Note:** Repository named as **"adapt_lanboun"**.  
## [Object Detection](https://git.hs-coburg.de/ADAPT/adapt_obj)
The object detection algorithms use visual data such as images, videos, and laser scan points to analyze and identify objects' locations. Identifying and understanding the surrounding environment is essential for safe vehicle navigation and parking. As a result, the information produced by the object detection process is provided to the Environment model.
> :memo: **Note:** Repository named as **"adapt_obj"**. 
## [Transmitter](https://git.hs-coburg.de/ADAPT/adapt_trnsmtr)

> :memo: **Note:** Repository named as **"adapt_trnsmtr"**. 
## Initial setup
```bash
cd adapt_main
vcs import src < adapt_repos.repo