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



##### Deliverable #2 - Active Learning Algorithm and Classification Task

1. The web application shall allow users to upload a reference video from their local machines. 


2. (Optional) The web application shall allow users to create multiple projects on the same video without repetitive uploads. If the same uploaded video is detected, the system shall inform users of existing projects related to the video. 

3. After the video is uploaded, the video is converted to a series of frames. The web application shall add a timestamp to each frame automatically. 

4. The web application shall allow users to choose a frame or upload another image from their local machines as a sample image. 

5. The active learning algorithm shall take  the sample image as training data for the first training iteration. 


6. After the first iteration is finished, the web application shall display a number of images with their timestamps queried by the active learning algorithm from the backend database, of which the number is determined by the length of video uploaded by the users. That is to say, the longer the video is, the more images will be proposed by the algorithm. 


7. The web application shall allow users to label each image displayed. 

8. The web application shall allow users to submit labeled (ticked) and unlabeled (un-ticked) images back to the active learning algorithm for training. 

9. After several iterations, the web application shall indicate that the algorithm training process is done. 

10. All images containing the target object shall be shown to users, and they shall be able to to be sorted based on their timestamps. 

11. The web application shall allow users to download the selected images.  

12. The web application shall ask  if users want to download the algorithm that is done training. 


13. (Optional) The web application shall be able to be saved by users whenever they feel like to exit the training process by clicking the button ‘Save Project’. 



## Non-Functional Requirements

Set of specifications/requirements that constraints/restricts in order to attempt to improve functionality against different backlogs. Non-functional requirements are also known as Backlog constraints. This is to make sure that our software system follows legal and adherence rules, and specifically specifies the attributes of the software. Here are some non-functional requirements our team has agreed to, to ensure a production of a good user experience software with ease of operating the software.

##### Performance
        Website should take no longer than 1 second to load
        Active Learning Algorithm should be able to query database within 1-2s

##### Security
        Software will not save data automatically, this will be an option to user
        Database will only store filepath, hence images will not be floating around in cloud
        Real images will be stored locally, confidential data is kept local

##### Reliability
        Software will be able to handle large amount of image processing without failure
        Ensure software will be able to classify image as close to 100% accuracy
        Ensure consistency in input processing and output over the lifecycle of the software

##### Usability
        Website will be simple and easy to navigate and browse around
        Intuitive features will be integrated to website such as magnifying glass to zoom into image

##### Robustness
        Software will catch any invalid input to avoid any processing problems
        Prevent any unwanted behaviors when image processing or learning algorithm is under progress



## Environmental Constraints

In software development, constraints are restrictions on the degree of freedom the developers are offered  in implementing a solution. They are effectively global requirements that specify device capabilities, system representations for which the application will be operated on. For our project, our client from ROSEN has detailed a series of constraints that we will adhere to when developing the application. We have classified the requirements into three classes:

##### *Programming Language and Framework Constraints*
The target users for our web application are mainly data scientists from ROSEN, whose programming background revolves heavily around Python. To ease daily user interaction and future maintenance, the client has requested our team to use Python as the main development language. Our client also requested the use of Javascript when developing the web application. Though not required, frameworks such as Dash, D3 and Plotly are recommended to us for adding features to the application.


##### *Equipment Constraints*
The client has required the application to be operable on a standard data scientist development system with the following configuration:
Laptop: CPU - Intel core i5/i7 11th gen, RAM - 16GB, Hard-disk space - 256GB SSD
Desktop: CPU - Intel core i5/i7 11th gen, RAM - 16/32GB, Hard-disk space - 512GB/1TB SSD



# Tech Stack
## Front-End Technologies
##### *Python*
We will use python with its libraries to render HTML pages into our website
Flask uses Jinja2 library to expand its functionality for its template engine. We will also make use of Mako (another library from Flask) to support Flask for the client-side purposes

##### *JavaScript, HTML, CSS*
JavaScript is a client-side programming interpreted language, so it is capable of reducing response time. Since performance plays a great part in the web application, JavaScript would be a good choice. 
HTML will be used for general displaying of content and structure of our website to the client
CSS will be used for styling and purposes to follow ROSEN’s general rules to clean code.
All team members have pre-requisite knowledge with these tools. Therefore, it is feasible to implement and has better maintainability.  

## Back-End Technologies
##### *Flask*
A micro web framework written in Python with powerful tools and libraries. We will use flask as a back-end tool to run the server side of the project.
All team members have pre-requisite Python knowledge. 

## Data Storing System
##### *MySQL Database*
Our project will implement MySQL database in our project for the following reasons:
MySQL is renowned for being a secure and reliable database management system used in popular web applications. This project can greatly benefit from MySQL since the software involves frequent image transfer and processing.
Our application is required to cope with 500,000 frames and MySQL offers great scalability to facilitate large amounts of data. 
Our development team aims to use the database to store file paths to images and other image related information such as timestamps and labels. We wish to avoid storing images in the database as it is highly inefficient.


## Image Processing
##### *VGG-16*
VGG16 will be used in our project for image processing of the sample image that is the reference to the object we intend our Active Learning Algorithm to be able to classify
It is a Convolutional Neural Network that will be able to chop our input image into 16 layers with 4096 high-dimensional pixels. With this, we will be able to find using its neighboring points any images that are similar amongst the images in our database.


## Prototype Modeling and Simulation
##### *Blender*
Blender will be used for prototype modeling and simulation. It is an open-source software for 3D computer graphics, and has rendering and animation capabilities. It can also be used as a video editor and for compositing.
Blender is free and flexible, and has many tools to aid the user in creating 3D models. It has been recommended by the client to create simulation prototypes of the water pipeline with debris inside.


## System Testing

##### Unit Testing Methodologies

For our project we will be using PyUnit for unit testing as Python will be mainly used in the backend, including the active learning algorithm. PyUnit testing includes various functions such as setUp() and tearDown(), which will be used to define the prerequisite and cleanup steps respectively. 
We will also be defining many other test cases. Examples of tests for our project are as follows:
- Check if  a minimum of 60% of all objects in the water pipeline video footage are detected
- Check if VGG-16 converts the sample image to a vector of 4096 dimensions
- Check if timestamp matches the correct video frame
- Check if ALA accepts labeled images as input
- Check if ALA Queries add 10 new images that have not been queried before
One possible way of  structuring the unit tests is with an AAA approach - Arrange, Act. and Assert. First, we would arrange the setup and initialization of the test. Then, we would perform the action of the test. Lastly, we would assert that the test has the expected outcome.

##### Quality Assurance in Accordance with Tech Stack
In order to ensure we are meeting quality standards, we will need to frequently evaluate the software system whether it meets the specified requirements or not. A variety of tests will be performed to ensure our software runs as intended. We intend to make our unit tests readable, repeatable, isolated, and deterministic.

We will practice regression testing to ensure existing code still runs correctly. This means that we will promptly correct any errors that emerge while testing our code. Regression testing will involve re-executing our test cases which may have passed before. Often, new changes can break older code, so this verifies that the newer code is compatible with the already existing codebase.


##### Continuous Integration
Continuous integration is the practice of regularly merging code into the main branch of the repository, as well as regularly testing code. This practice will allow for automated testing as well. A strategy we may use is to get a continuous integration tool to streamline the continuous integration process. One possible tool is GitLab, which has features such as team planning tools and merge trains.


## Frequently Asked Questions

**Q:** Will there be any login information for the users?
**A:** There won’t be any login information for users as we have specifically addressed this issue. According to our client, this web application will only be used within the Rosen group.

**Q: **Are there other customers or is it just for the client? Any other user groups to consider?
**A:** The application that we are developing is specially catered for data scientists working in ROSEN. Another potential user group will be the data evaluators working in ROSEN to ensure that the data source and the outputs are valid. It will be up to the client to decide if they want to make the application available for other users. 

**Q: **How will you store your images?
**A: **Images will be stored locally on the user’s environment as the client specified that we will not be using a server.



**Q:** Do you plan to use pure JavaScript for the front end or do you plan to use a specific framework?
**A:** Yes, aside from JavaScript, HTML and CSS will also be used for front-end development. Although the client has suggested we also use Dash when developing the front-end, our group decided to not use it. Since the expected outcome won’t include data visualizations, Dash is useless for our project.  

**Q:** Why is it a web app if the target user is a Rosen Data scientist? Can’t you just give them the program itself as a script?
**A:** The client has requested us to create an interface for data scientists to streamline the classification process, which
would otherwise run as a script. This is because there are images and buttons the client will click, and we would like to add functionality relating to viewing the video frames.

**Q: **Will simulation data be manually generated? How long do you expect data generation to take?
**A:** The simulation data will be manually generated using Blender. We will either have to create a pipeline prototype with debris from scratch, find free models with a Creative Commons license, or a combination of both. We don’t have an exact timeframe, but we expect this process to take at least a couple of weeks.

**Q:** Do you need to train the model or is it pretrained?
**A: **The model is not pre-trained, or might be trained to a certain extent. Our intention of this project is to train our model, in our case, the Active Learning Algorithm, which will be able to classify objects by using an image as a reference, and learning it from a pool of images in the database.

**Q:** Are there guests that will be visiting this web application or is it only for other data scientists or people in ROSEN?
**A: **No. There will be no guest visiting the web application.  The project will be made so that it will be able to run on the ROSEN network. The web application will be made with the intention to only be able to be run locally for our end users, who are data scientists in the ROSEN for algorithm training purposes. However, if they choose to, people in ROSEN will be able to visit the web application.
