# Importing the proper classes
from DeepImageSearch import Index,LoadData,SearchImage
import os
import time
# load the Images from the Folder (You can also import data from multiple folders in python list type)
image_list = LoadData().from_folder(['./DeepImageSearch/images'])

# For Faster Serching we need to index Data first, After Indexing all the meta data stored on the local path
# added this to skip prompting user. So when user click 'run' in front-end, it will automatically answer yes to the prompt

def imageSearch():
        start = time.time();
        if 'meta-data-files' not in os.listdir('.'):
                Index(image_list).Start()
        # for searching, you need to give the image path and the number of the similar image you want
        print(SearchImage().get_similar_images(image_path=image_list[0],number_of_images=5))

        end = time.time();

        print(end-start);


# If you want to plot similar images you can use this method, It will plot 16 most similar images from the data index
# SearchImage().plot_similar_images(image_path = image_list[0])

imageSearch()