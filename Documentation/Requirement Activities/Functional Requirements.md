# Functional Requirements 
## Deliverable #1 - Web User Interface
1. The system should be a web application with a user interface.
2. The web user interface shall have a button ‘Upload video’ for users to browse videos on their local machines and select one. 
3. After the video is selected, the web user interface shall have a ‘Confirm’ button for users to confirm uploading. 
4. After the video is uploaded, the web user interface shall have two buttons: ‘Choose a local image’ and ‘Choose an image from video’. 
5. If users on ‘Choose an image from video’, a dialogue box of all frames will be prompted. Users shall scroll down, select one frame and click on the ‘Confirm’ button for confirmation. 
6. After the sample image is uploaded, the active learning algorithm takes it as its training data for the first training process iteration. During the processing phase, a loading page will be displayed. 
7. After the first iteration is finished, the web application shall display a number of images with their timestamps. 
8. The web user interface shall allow users to label each image displayed by using tick-boxes. The options of ‘Select All’ and “Deselect All’ should be given to users. Images that are ticked by users are labeled ‘Interested’, those un-ticked are labeled ‘Not Interested’. Images that are labeled ‘Interested’ should include target objects. 
9. After the labeling process is done, the web user interface shall allow users to submit labels by clicking the ‘Submit’ button.
10. The web user interface shall be able to display all images containing target objects. Users shall be allowed to sort images according to their timestamps by clicking the sort button. 
11. The web application shall allow users to download the selected images by clicking the button ‘Download’. 
12. The web user interface shall prompt a dialogue box asking if users want to download the algorithm that is done training.

## Deliverable #2 - Active Learning Algorithm and Classification Task
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






