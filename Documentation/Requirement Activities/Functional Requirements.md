# Functional Requirements 
### 1. Selecting a video from the local machine
  - Firstly, our application will access users' local file systems for browsing video files. 

### 2. Uploading a video to the software
  - Our product must allow users to select and upload a video file for their classification tasks. The video will be cut into a series of frames. 

### 3. Uploading a sample image of an object which user is interested in
  - After the video is chopped into a series of frames, the user will upload a sample image of an object which user is interested in (for example, fish or AmEX ceilings in the pipelines)

### 4. Creating one or more projects on the same video
  - After the sample image has being uploaded, the system shall allow users to create multiple projects on the same video. 

### 5. Presenting 10 images to users and they can label the ones including the object
  - The software will propose 10 images and let users decide whether those images have the specified object respectively. If they are checked, they are labeled with 'yes'. The unchecked ones are marked 'no'. 
  - After users have finished labeling this round, the 10 images will be fed back to the active learning algorithm. The algorithm will be trained, and in the next round, another 10 images are displayed and users will repeat the same labeling process. 
  - After couple of iterations, the algorithm will be smart enough to find all images including the specified object. 

### 6. Showing the timestamp of every image
  - The system will automatically add a timestamp to each image.

### 7. Sort images according to timestamps
  - All images can be sorted by their accordingly timestamps, either in ascending or desending order.

### 8. ALL images with the target object will be displayed in the browser
  - All images that are categorized as including the target object will be displayed to users.

### 9. Downloading selected images to users’ local machines
  - Finally, the displayed images must be able to be selected and downloaded for users' further use. 






