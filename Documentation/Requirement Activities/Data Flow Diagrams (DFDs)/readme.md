# Data Flow Diagrams

In this folder, you will be able to see our project's Data Flow Diagram (Level 0 and Level 1).
This is made to view the flow of information for our software from user input, to the end result.

*[NOTE]: This is to be changed one scope is refined*
## Explanation For DFD 0
DFD 0 is intended to explain the high-level overview of the flow of our program.

1) User will be asked to provide input to interact with our software for training algorithm purposes
2) Software will be well-trained to classify image given as input

## Explanation for DFD 1
Here's is more in-depth explanation or flow of our program.

1) User will provide 2 inputs as part of the whole program
    a. Sample reference of image as an interested object that our ALA will be able to classify (Directly to the website)
    b. Videos or pools of images that will be the source of the learning algorithm (Indirectly - i.e: once processed, then to the website)

2) Input a. will undergo image processing through VGG16, chopped up into layers of images
3) This layer of images will be used as an input to the ALA
4) On the other hand, we create prototype modelling using blender that will create a video
5) This video will be processed into vectors of images, passed to the website, stored in the local (images) and database (pathfile to images)
*Below will be an iterating process once all the input is given to the ALA*
6) ALA will query images from the input given in number 3), producing 10 images that the ALA think is similar
7) These images will be shown in the web interface, where users will be able to help manually label which ones are the similar objects
8) These pools of labelled similar and dissimilar objects will be given back to the ALA, and the process repeat

9) Once a certain iteration is finished, all similar objects based on our ALA will be produced in the web interface
10) At this point, we expect the ALA is good enough to classify objects similar to the sample reference, hence learning stops and user will receive a well-trained active learning algorithm that classifies objects similar to sample reference (i.e: Input 1a.)
