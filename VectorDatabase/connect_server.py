# ==== milvus libraries ====
import os
from os import getcwd
from datetime import datetime

from pymilvus import connections, Collection, FieldSchema, DataType, CollectionSchema, utility
# ==== milvus libraries ====

# ==== vgg16 libraries ====
import keras
from keras.applications.vgg16 import VGG16 as vgg16
from keras.models import Model
import cv2

# ==== vgg16 libraries ====

fmt = "\n=== {:30} ===\n"
connections.connect(
    alias="default",
    host='localhost',
    port='19530'
)

has = utility.has_collection("image")
print(f"Does collection image exist in Milvus: {has}")

if has:
    utility.drop_collection("image")

# Field schema
id_field = FieldSchema(name="id",
                       dtype=DataType.INT64,
                       is_primary=True,
                       auto_id=True,
                       description="primary id"
                       )
path_field = FieldSchema(name="path",
                         dtype=DataType.VARCHAR,
                         max_length=1024
                         )
timestamp_field = FieldSchema(name="timestamp",
                              dtype=DataType.VARCHAR,
                              max_length=512
                              )
size_field = FieldSchema(name="size",
                         dtype=DataType.DOUBLE
                         )
label_field = FieldSchema(name="label",
                          dtype=DataType.BOOL
                          )
vector_field = FieldSchema(name="vector",
                           dtype=DataType.FLOAT_VECTOR,
                           dim=4096,
                           description="vgg16 vector"
                           )
fields = [id_field, path_field, timestamp_field, size_field, label_field, vector_field]
# Collection schema
collection_schema = CollectionSchema(fields)

print(fmt.format("Create collection `image`"))

# Collection
collection_name = "image"
collection = Collection(
    name=collection_name,
    schema=collection_schema
)

list = utility.list_collections()
print(fmt.format(f"List collections in this Milvus instance: {list}"))

has = utility.has_collection("image")
print(f"Does collection image exist in Milvus: {has}")

# ======= store fc2 layer vector into the vector database ======

# creating VGG16 model
model = keras.applications.VGG16(weights="imagenet", include_top=True, pooling="max", input_shape=(224, 224, 3))

# removing last layer; model is up to fc2 (second last layer)
model_fc2 = Model(inputs=model.input, outputs=model.get_layer("fc2").output)

# create a folder for storing frames
path = os.getcwd() + "/frames" # get current working dir
os.mkdir(path)

# function to convert a video to a series of images
def extractImages(pathIn):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success, image = vidcap.read()
    success = True
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC, (count * 1000))  # added this line
        success, image = vidcap.read()
        # print('Read a new frame: ', success)
        if not success:
            break
        cv2.imwrite(os.path.join(path, "frame" + str(count) + ".jpg"), image)  # save frame as JPEG file
        count = count + 1

extractImages("video.mp4")



# function to convert image to vector of 4096 dimensions
def getVector(img):
    # initial image dimensions
    # print(img.shape)
    # resizing and reshaping image to fit input shape
    img = cv2.resize(img, (224, 224)).reshape(1, 224, 224, 3)
    # resized and reshaped dimensions
    # print(img.shape)
    # retrieving vector for image
    vector = model_fc2.predict(img)
    return vector

# function to vectorize frames and store them into the database
def vectorizeFrames(pathIn):
    for frames in os.listdir(pathIn):
        if frames.endswith("jpg"):
            # vectorize frame
            framePath = os.path.join(pathIn, os.path.basename(frames))
            frameName = os.path.abspath(framePath) # frame path
            frameTimeStamp = datetime.now().strftime("%H:%M:%S") # frame timestamp
            frameSize = os.stat(frameName).st_size / 1000 # frame size in KB
            frameLabel = False # if this frame is labelled
            frameVector = getVector(cv2.imread(frameName)) # frame vector
            # insert vectors into the DB
            frameData = [
                [frameName],
                [frameTimeStamp],
                [frameSize],
                [frameLabel],
                frameVector]
            collection.insert(frameData)
            print(fmt.format(os.path.basename(frames) + " vector inserted into `image`"))
    return

vectorizeFrames(path)

# load image
sampleImage = cv2.imread("fish.jpg")
# image name
imageName = os.path.abspath("fish.jpg")
# image timestamp
imageTimeStamp = datetime.now().strftime("%H:%M:%S")
# image size in KB
imageSize = os.stat(imageName).st_size / 1000
# image label
imageLabel = False
# vectorize image
imageVector = getVector(sampleImage)

data = [
    [imageName],
    [imageTimeStamp],
    [imageSize],
    [imageLabel],
    imageVector]
collection.insert(data)
print(fmt.format("Sample image vector inserted into `image`"))

print(fmt.format("Drop collection `image`"))
utility.drop_collection("image")
