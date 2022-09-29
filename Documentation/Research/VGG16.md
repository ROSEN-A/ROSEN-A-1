# VGG16

## What is VGG16?
- VGG-16 is a convolutional neural network that is 16 layers deep. You can load a pretrained version of the network trained on more than a million images from the ImageNet database [1]. 
- The pretrained network can classify images into 1000 object categories, such as keyboard, mouse, pencil, and many animals.
- As a result, the network has learned rich feature representations for a wide range of images. The network has an image input size of 224-by-224.

## What is VGG16 used for?
- Object detection and classification algorithm
- Able to classify images from 1000 different categories with 92.7% accuracy
VGG16 Architecture
- The 16 in VGG16 refers to 16 layers that have weights. In VGG16 there are thirteen convolutional layers, five Max Pooling layers, and three Dense layers which sum up to 21 layers but it has only sixteen weight layers i.e., learnable parameters layer.
- VGG16 takes input tensor size as 224, 244 with 3 RGB channel
- Most unique thing about VGG16 is that instead of having a large number of hyper-parameters they focused on having convolution layers of 3x3 filter with stride 1 and always used the same padding and maxpool layer of 2x2 filter of stride 2.
- The convolution and max pool layers are consistently arranged throughout the whole architecture
- Conv-1 Layer has 64 number of filters, Conv-2 has 128 filters, Conv-3 has 256 filters, Conv 4 and Conv 5 has 512 filters.
- Three Fully-Connected (FC) layers follow a stack of convolutional layers: the first two have 4096 channels each, the third performs 1000-way ILSVRC classification and thus contains 1000 channels (one for each class). The final layer is the soft-max layer.

## Use cases of OpenCV
-	Image Recognition or Classification 
    – VGG16 can be used for disease diagnosis using medical imaging like x-ray or MRI. 
-	Detecting street signs and moving vehicle
    - It can be used in recognizing street signs from a moving vehicle.
-	Image Detection and Localization 
    - VGG16 performs really well in image detection use cases. 
-	Image Embedding Vectors –
    - After popping out the top output layer, the model can be used to train to create image embedding vectors which can be used for a problem like face verification using VGG16 inside a Siamese network. 

## Advantages of VGG16
- Accuracy of VGG16 is known as one of the best in training model
- Don't require mastery in Deep Learning to use pretrained models.
- Easily modify use cases to align with requirements
- It will be more efficient in terms of size and training time(because there may be less number of layers as compared to any pretrained model trained for more than one purpose)
- Popular tools that can be easily embedded and/ train in many softwares such by
    - MATLAB
    - Keras
    - Tensorflow

## Why do we need this tool for the project?
- Client deals with water inspections using the tool that takes snapshots in 360 degrees flowing in a pipeline from one end to the other
- Client needs to detect and filter objects which will be used to filter thousand or millions images from database
- VGG16 can be trained to achieve the intended goal of the objects to be filtered such as leaves, roots, trashes, fishes, etc..

# How to use VGG16? 
- There are different way to train VGG16 model, the most common ones are:
    - Keras
    - Tensorflow
- With these tools, which is easily embedded in Python, which will be our main backend, this tool is very helpful to filter images as needed from the datasource, once it’s trained