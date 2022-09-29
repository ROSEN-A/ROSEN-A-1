# Client Meeting I

**Date:** September 27, 2022

**Attendees:** Orvin Tritama, Qingyan Hu, Ryan Lu, Fareeha Hayat (Sick Leave)

**Location:** COM007

**Goal:** First meeting with client, discuss project details with the client.


<br>


## Discussion Notes

- There will be two independent deliverables to this project.  (both from scratch)

	- One deliverable will be **implementation of the active machine learning algorithm**. 
		
	- The other major deliverable will be the **working web application**.
		
- The web application will be dedicated to classifying the objects and debris present inside the water pipeline.

- The web application will have no authentication, security requirements as this web app will be used among ROSEN data scientists.

- The application is preferably implemented in **Python** for easier maintenance in the future.



## How the Web Application will work

1. A data scientist from ROSEN will upload a sample photo into the web application (the user may be able to create labels to classify what he/she is looking for) The user may also input vectors that contain photos.

2. The active learning algorithm will analyze the picture and find all similar pictures from a database that matches the uploaded picture. The system will pick 20 relevant pictures to output.

3. The user will be able to save and download the relevant information to its local machine. The information can be pictures, as well as CSV files that contain the photo vector. (the output is unclear as of yet)



## Actionable steps to development

- **Blender**: This will be our main tool for prototyping. We will use Blender to generate simulations of different debris inside the water pipelines. These data will be used to train our machine learning algorithm

- **Research** implementable ML algorithms. A suggested option is VGG16 network encoder. From the meeting, the **ML algorithm seems to be the priority**. 



<br>


*Future meetings will be held at Tuesdays 1:30pm, location remains TBD. Future meetings may be held as online meetings via Microsoft Teams.*


