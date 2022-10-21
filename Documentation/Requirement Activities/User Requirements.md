# User Requirements

The user requirements are the specification of what the user does to the software system.


---


1. The user will open the web application through their browser, in this case Google Chrome.


2. The user will upload video footage of a water pipeline inspection to classify, as well as a sample image of an object of interest (i.e. a fish or leaf).

- They browse through their local file system to select which video files to classify, as well as the sample image.

- They have the option to upload multiple files at the same time.


3. The user will confirm to start processing the selected files (by pressing a confirmation button, for example).

- The application will convert the video files to image frames, and then it will run the algorithm.

- They wait for the classification process to finish, and the algorithm does not need to be supervised by the user (because it has been pre-trained in the development phase).


4. The user will view the feedback of the now classified video frames.

- The application will show any images of the video frames that have the object of interest detected.

- The user can click to pan around the images of the video frames to center on the object found.

- The user can also click a button to zoom into the images of the video frames to further inspect the area (and also click a button to zoom out).

