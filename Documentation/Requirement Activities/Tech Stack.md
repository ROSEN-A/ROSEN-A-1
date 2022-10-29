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
#### *Flask*
A micro web framework written in Python with powerful tools and libraries. We will use flask as a back-end tool to run the server side of the project.
All team members have pre-requisite Python knowledge. 

## Data Storing System
#### *MySQL Database*
Our project will implement MySQL database in our project for the following reasons:
MySQL is renowned for being a secure and reliable database management system used in popular web applications. This project can greatly benefit from MySQL since the software involves frequent image transfer and processing.
Our application is required to cope with 500,000 frames and MySQL offers great scalability to facilitate large amounts of data. 
Our development team aims to use the database to store file paths to images and other image related information such as timestamps and labels. We wish to avoid storing images in the database as it is highly inefficient.


## Image Processing
#### *VGG-16*
VGG16 will be used in our project for image processing of the sample image that is the reference to the object we intend our Active Learning Algorithm to be able to classify
It is a Convolutional Neural Network that will be able to chop our input image into 16 layers with 4096 high-dimensional pixels. With this, we will be able to find using its neighboring points any images that are similar amongst the images in our database.


## Prototype Modeling and Simulation
#### *Blender*
Blender will be used for prototype modeling and simulation. It is an open-source software for 3D computer graphics, and has rendering and animation capabilities. It can also be used as a video editor and for compositing.
Blender is free and flexible, and has many tools to aid the user in creating 3D models. It has been recommended by the client to create simulation prototypes of the water pipeline with debris inside.
