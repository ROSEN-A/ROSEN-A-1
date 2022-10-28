# COSC499 Capstone Software Engineering Project - ROSEN A


**Team members:** `Qingyan Hu`  `Orvin Tritama`  `Fareeha Hayat`  `Ryan Lu`


## Introduction


### Project Description

The project will develop a web application offered to the data scientists working in the ROSEN Group and will seek to simplify data scientist’s workload in classifying concerned objects within a water pipeline while advancing the accuracy in detection. Users will be able to utilize the software to classify large amounts of images from a video recorded by the water pipeline inspection system in a highly efficient manner. The concerned objects will not be predefined by the software, instead the users are able to define the objects they are interested in, such that the web application would be vastly versatile in detecting the user-defined objects. The web application will be supported by an active learning algorithm that will use a vectorized sample image as reference to classify the video frames uploaded by the user.


### Target Users

##### *Data Scientists*
The project is catered for data scientists working for the ROSEN Group. These individuals are fluent in the Python programming language and they will use our web application in pipeline inspection projects to find interested items within the water pipeline. 

##### *Data Evaluators*
The project can be used by data evaluators working in the ROSEN Group. These individuals are likely to be working in a team to evaluate the integrity of the data source as well as the output of the web application.


### Project Scope
Our development team plans to decompose the project into two major deliverables, web user interface and the active learning algorithm. The deliverables will cover research, documentation, development and optimizing the components. Based on the client requirements, our focus will be on the active learning algorithm, rather than the user interface. It is also noted that the active learning algorithm does not need to be optimized. Our development team will specifically focus on one object class detection for this project.



## Project Milestone

### Milestone 1
This particular milestone represents that the  project scope and requirement has been agreed upon between our team and the client. We host the requirement presentation with our client and make sure that all required features are clear and achievable. By October, we will submit the requirements report to the instructor and begin our project development.


### Milestone 2
Our aim is to present a functioning web user interface by December, by which the user interface will be available to the client and peers for feedback. Though our focus is on the user interface, the active learning algorithm will be developed concurrently.


### Milestone 3
The main objective of milestone 3 is to complete the implementation of our active learning algorithm as well as refining our user interface based on the feedback we received from milestone 2. We will also begin integrating our machine learning algorithm into our web application.


### Milestone 4
By February 2023, we will finish our implementation and testing phase for our software. The fully functional web application will be available to the client and peers to review. We will perform our hand-off session with the client which will mark the completion of our capstone project.



## Data Flow Diagram




## Functional Requirements

##### Deliverable #1 - Web User Interface

1. The system should be a web application with a user interface.


2. The web user interface shall have a button ‘Upload video’ for users to browse videos on their local machines and select one. 

3. After the video is selected, the web user interface shall have a ‘Confirm’ button for users to confirm uploading. 

4. After the video is uploaded, the web user interface shall have two buttons: ‘Choose a local image’ and ‘Choose an image from video’. 

5. If users on ‘Choose an image from video’, a dialogue box of all frames will be prompted. Users shall scroll down, select one frame and click on the ‘Confirm’ button for confirmation. 

6. After the sample image is uploaded, the active learning algorithm takes it as its training data for the first training process iteration. During the processing phase, a loading page will be displayed. 

7. After the first iteration is finished, the web application shall display a number of images with their timestamps. 

8. The web user interface shall allow users to label each image displayed by using tick-boxes. The options of ‘Select All’ and “Deselect All’ should be given to users. Images that are ticked by users are labeled ‘Interested’, those un-ticked are labeled ‘Not Interested’. Images that are labeled ‘Interested’ should include target objects. 

9.  After the labeling process is done, the web user interface shall allow users to submit labels by clicking the ‘Submit’ button.

10. The web user interface shall be able to display all images containing target objects. Users shall be allowed to sort images according to their timestamps by clicking the sort button. 

11. The web application shall allow users to download the selected images by clicking the button ‘Download’. 

12. The web user interface shall prompt a dialogue box asking if users want to download the algorithm that is done training.



## Non-Functional Requirements





## Environmental Constraints




## Tech Stack




## System Testing





## Frequently Asked Questions