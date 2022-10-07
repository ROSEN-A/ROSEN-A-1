## Image Object Detection
### COCO (Microsoft Common Objects in Context)
- The MS COCO dataset is a large-scale object detection, segmentation, key-point detection, and captioning dataset. The dataset consists of 328K images.
- The dataset has annotations for:
  1. Object detection
      -  bounding boxess and per-instance segmentation masks with 91 object categories (as listed in file 'coco.names')
  2. Captioning
      - natural language description of images  
  3. Keypoints detection
      - containing more than 200,000 images and 250,000 person instances labeled with keypoints
### frozen_inference_graph.pb
- Freezing is the process to identify and save all of required things in a single file for easier use. 
- A frozen graph that cannot be trained anymore, it defines GraphDef and is in reality a serialized graph. 
### ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt
- The mobilenet-ssd model is a Single-Shot multibox Detection (SSD) network, intended to perform object detection. 
- In simple words, this file is a pre-trained Tensorflow model and has already been trained on the COCO dataset.



