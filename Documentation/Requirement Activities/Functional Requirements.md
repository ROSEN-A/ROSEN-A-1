# Functional Requirements 
### 1. Selecting a video from the local machine
  - Firstly, our application will access users' local file systems for browsing video files. 

### 2. Uploading a video to the software
  - Our product must allow users to select and upload a video file for their classification tasks. The video will be cut into a series of frames. 

### 3. Uploading a sample image of an object which user is interested in
  - After the video is chopped into a series of frames, the user will upload a sample image of an object which user is interested in (for example, fish or AmEX ceilings in the pipelines)

### 4. Creating one or more projects on the same set of images
  - After the sample image has being uploaded, the system shall allow users to create multiple projects on the same video. 

### 5. Displaying a set of images with object(s) defined by users
  - The system will proccess and classify images using a trained active learning algorithm togetehr with pre-trained machine learning algorithms. 
  - After process is finished, relevant images (images including object(s) which users are interested in) will be displayed. 

### 6. Showing the timestamp of every image
  - The system will automatically add a timestamp to each image.

### 7. Sort images according to timestamps
  - All images can be sorted by their accordingly timestamps, either in ascending or desending order.

### 8. Downloading selected images to users’ local machines
  - Finally, the displayed images must be able to be selected and downloaded for users' further use. 






