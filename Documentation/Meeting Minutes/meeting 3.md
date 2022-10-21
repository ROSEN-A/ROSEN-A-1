# Client Meeting III

**Date:** October 18, 2022

**Attendees:** Orvin Tritama, Qingyan Hu, Ryan Lu, Fareeha Hayat

**Location:** Microsoft Teams

**Goal:** Present our presentation, ask for client feedback and clarify project specifications.


<br>


## Discussion Notes
        To the client, the presentation was not very impressive. There was a clear misunderstanding between our team and the client.


        Based on the client's feedback, what he wanted for the project was far from what we understood. The requirements were different, and the development process was also questioned.


        The client wants us to prioritize the development of the active learning algorithm and the web interface is of less importance compared to the ML algorithm




## How the Web Application will work
        Based on this week's meeting, we have a new understanding of how the web user interface should look like based on the requested input from the user.


        Firstly, the user will upload a video of the water pipeline.


        Then, the system will chop up the video into thousands of frames and that will be save to the local file system.


        The user will then input a sample image of what they are looking for. For example, the user may be looking for fishes inside the water pipeline, then the sample image will include the fish object.


        Our web application should be able to detect the objects in the sample image.


        Based on the sample image, the application will be able to return 10 images from the video frames that the system thinks is related to the sample image.


        The user will then select the ones that the user is interested in. At this point, the returned images are labeled with interested and non-interested.


        this loop will be executed for a few times until the system is smart enough to correctly label all the images.




## Actionable steps to development
        The client has specified that we start developing the active learning algorithm first and then worry about the web user interface because he thinks that the web application is not important at all and that all it matters is that the machine learning algorithm works properly and accurately.


        We first will start off with creating a prototype using Blender. This will be really important for the future of this project. A working prototype of the water pipeline shuold be set up properly to train our machine learning algorithm.




<br>
