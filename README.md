<p align="center">
        <img src="https://user-images.githubusercontent.com/77523948/229239097-366ce370-49a0-494f-8680-f1414b8b3e50.png" width="500" height="250">
</p>

<h1 align="center">
        COSC499 Capstone Software Engineering Project - ROSEN A
</h1>

<h4 align="center">
        <b>Team members:&nbsp;</b> Qingyan Hu&nbsp;&nbsp;&nbsp;&nbsp;Orvin Tritama&nbsp;&nbsp;&nbsp;&nbsp;Fareeha Hayat&nbsp;&nbsp;&nbsp;&nbsp;Ryan Lu

</h4>


<br>

# Project Setup [IMPORTANT]
How to run our code?

### Requirements: 
- Python version 3.9 can be found [here](https://www.python.org/downloads/release/python-3916/)
- Flask version 2.2.2 can be installed using `pip install flask==2.2.2`
- DeepImageSearch Library can be installed using `pip install DeepImageSearch`
- natsorted library can be installed using `pip install natsort`
- opencv library can be installed using `pip install opencv-python`
**Note:** Installing DeepImageSearch might fail due to error in `annoy` package as DeepImageSearch utilizes this package. 
Here are the steps to fix this problem:
1) Navigate to https://visualstudio.microsoft.com/downloads/
2) Scroll down to *All Downloads* and find *Tools for Visual Studio*
3) Download *Build Tools for Visual Studio 2022*
4) Run the program
5) Under *Workloads* find *Desktop development with C++*
6) By default, the first 5 options under *optional* are checked
7) Run install
8) Restart computer, and rerun `pip install DeepImageSearch`

<br>

### How to run the application?
1) Navigate to our website directory through console `cd Website`
2) Run this code `python server.py`
3) You will see output similar to 
``` 
* Serving Flask app 'server'
* Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
* Running on http://127.0.0.1:5000
```
4) Head to google chrome and copy paste `http://127.0.0.1:5000` or Hold left `ctrl` and click on the link given


<br>

### What does the program do and how to use it?
1) First page is the **Login page** 
        - Enter *RosenA* as username and password and click login
        
2) Second page is the **Upload image page**
        - Click on **Choose Image** button to choose the *reference image* you would like to use for classification
        - Click **Upload** to save the image in the program
        - Click next to go to next page

3) Third page is the **Upload video page**
        - Click on **Choose Video** to choose the video you would like to be classified
        - Click **Upload** to save the image in the program
        - Click next to go to the next page

4) Last page will be the **Result page** where you will be able to see the corresponding result classified from uploaded video (3), using the reference image uploaded (2)


<br>

<h2 align="center">
        System Description
</h2>
We have developed a web application offered to data scientists working in the ROSEN  group that aims to simplify a data scientist’s workload in classifying concerned objects inside a water pipeline, while advancing the accuracy in object detection. The application utilizes an approximate-nearest-neighbors machine learning algorithm to classify large amounts of images from a video recorded by the water pipeline inspection system in a highly efficient manner. The concerned objects will not be predefined by the software, instead the users are able to define the objects they are interested in, such that the web application would be vastly versatile in detecting user-defined objects.


### Target Users

##### *Data Scientists*
The project is catered for data scientists working for the ROSEN Group. These individuals are fluent in the Python programming language and they will use our web application in pipeline inspection projects to find interested items within the water pipeline. 

##### *Data Evaluators*
The project can be used by data evaluators working in the ROSEN Group. These individuals are likely to be working in a team to evaluate the integrity of the data source as well as the output of the web application.

<br>


<h2 align="center">
        Tech Stack
</h2>

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
