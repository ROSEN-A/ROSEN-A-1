import shutil
from flask import Flask, render_template, redirect, url_for, request, abort, send_from_directory
import imghdr
import os
from werkzeug.utils import secure_filename
import deepImageSearch
from datetime import datetime
import cv2
# import deepImageSearch
from DeepImageSearch import Index,LoadData,SearchImage
import time
import glob
from zipfile import ZipFile
import requests


app = Flask(__name__)

# Config for extensions for video and images
app.config['PHOTO_EXTENSIONS'] = ['.jpg', '.png', '.jpeg']
app.config['VIDEO_EXTENSIONS'] = ['.mp4']

# Config for uploaded images/videos path
app.config['UPLOAD_PATH_IMAGE'] = './static/uploadedImage'
app.config['UPLOAD_PATH_VIDEO'] = './static/uploadedVideo'

# Config for extracted images from video
app.config['EXTRACTED_IMAGES'] = './static/extractedImages'

app.config['SIMILAR_IMAGES'] = './static/similarImages'


################################################ LOGIN PAGE ####################################################
# First rendered papge
@app.route('/')
def home():
    # DELETE ALL EXISTING FILES BEFORE PROGRAM STARTS
    # remove the index dir for deep image search
    if(os.path.exists('./meta-data-files')):
        shutil.rmtree('./meta-data-files')
    # remove the dir uploadedImage 
    if(os.path.exists('./static/uploadedImage')):
        shutil.rmtree('./static/uploadedImage')
    # remove the dir uploadedVideo
    if(os.path.exists('./static/uploadedVideo')):
        shutil.rmtree('./static/uploadedVideo')
    # remove the dir extractedImages
    if(os.path.exists('./static/extractedImages')):
        shutil.rmtree('./static/extractedImages')
    if(os.path.exists('./static/similarImages')):
        shutil.rmtree('./static/similarImages')
    
    # MAKE FILES FOR PROGRAM
    # make a dir for uploaded image
    os.mkdir('./static/uploadedImage')
    # make a dir for uploaded video
    os.mkdir('./static/uploadedVideo')
    # make a dir for extracted images from the uploaded video
    os.mkdir('./static/extractedImages')
    os.mkdir('./static/similarImages')

    return render_template('login.html')


# Login redirect to uploadImage() which renders uploadImage.html
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != 'RosenA' or request.form['password'] != 'RosenA':
            return home()
        else:
            return redirect(url_for('uploadImage'))


################################################ UPLOAD IMAGE PAGE ####################################################

# Setup the config to UPLOAD_PATH_IMAGE and renders uploadImage.html
@app.route('/uploadImage')
def uploadImage():
    files = os.listdir(app.config['UPLOAD_PATH_IMAGE'])
    return render_template('uploadImage.html', files=files)


# Get the file name of the uploaded file and save to ./static/uploadedImage folder
@app.route('/uploadImage', methods=['POST'])
def upload_files():

    ####### if the user returns to this page from result.html, every folder has to be empty ########
    # make a dir for uploaded image
    if(os.path.exists('./static/uploadedImage')):
        shutil.rmtree('./static/uploadedImage')
    os.mkdir('./static/uploadedImage')
    # make a dir for uploaded video
    if(os.path.exists('./static/uploadedVideo')):
        shutil.rmtree('./static/uploadedVideo')
    os.mkdir('./static/uploadedVideo')
    # make a dir for extracted images
    if(os.path.exists('./static/extractedImages')):
        shutil.rmtree('./static/extractedImages')
    os.mkdir('./static/extractedImages')
    # clear similarImages folder
    if(os.path.exists('./static/similarImages')):
        shutil.rmtree('./static/similarImages')
    os.mkdir('./static/similarImages')
    
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['PHOTO_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH_IMAGE'], filename))
    return redirect(url_for('uploadImage'))


# This method is called in uploadImage.html, loop over the images from UPLOAD_PATH_IMAGE and preview in the screen
# <img src="{{ url_for('upload_image', filename=file) }}">
@app.route('/uploadedImage/<filename>')
def upload_image(filename):
    return send_from_directory(app.config['UPLOAD_PATH_IMAGE'], filename)

# Function to check if there are files in the uploadedImage directory
@app.route('/uploadedImage')
def check_image_files():
    check = True
    if (len(os.listdir(app.config['UPLOAD_PATH_IMAGE'])) > 0):
       check = True
    else:
        check = False
    return render_template('uploadImage.html', check=check) # check if output is correct


################################################ UPLOAD VIDEO  PAGE ####################################################

@app.route('/uploadVideo')
def uploadVideo():
    files = os.listdir(app.config['UPLOAD_PATH_VIDEO'])
    return render_template('uploadVideo.html', files=files)


@app.route('/uploadVideo', methods=['POST'])
def upload_video():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['VIDEO_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH_VIDEO'], filename))
    return redirect(url_for('uploadVideo'))


# Function to check if there are files in the uploadedVideo directory
@app.route('/uploadVideo')
def check_video_files():
    check = True
    if (len(os.listdir(app.config['UPLOAD_PATH_VIDEO'])) > 0):
        check = True
    else:
        check = False
    return render_template('uploadVideo.html', check=check) # check if output is correct


# To be deleted later if not needed
# To be used similar to upload_image, but this will be called in uploadVideo.html to preview video
# @app.route('/uploadedVideo/<filename>')
# def upload_video(filename):
#     return send_from_directory(app.config['UPLOAD_PATH_VIDEO'], filename)


################################################ TO BE ADDED ####################################################
@app.route('/image')
def image():
    return render_template('image.html')


@app.route('/frames')
def frames():
    return render_template('frames.html')

#### loading ####
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
        cv2.imwrite(os.path.join(app.config['EXTRACTED_IMAGES'], "frame" + str(count) + ".jpg"), image)  # save frame as JPEG file
        count = count + 1

@app.route('/loading')
def loading():
    videoName = os.listdir(app.config['UPLOAD_PATH_VIDEO'])[0]
    videoFile = os.path.join(app.config['UPLOAD_PATH_VIDEO'], videoName)
    extractImages(videoFile)
    return render_template('loading.html')

##### processing ####
@app.route('/search')
def search():
    imagesFrameList = deepImageSearch.imageSearch('./static/uploadedImage','./static/extractedImages', 10)

    # Save all extractedFiles in the cv_image
    cv_img = []
    for img in glob.glob("./static/extractedImages/*.jpg"):
        n= cv2.imread(img)
        cv_img.append(n)

    
    # write all similar files indexed at imagesFrameList, and stored at cv_img to app.config['SIMILAR_IMAGES']
    for i in imagesFrameList:
        cv2.imwrite(os.path.join(app.config['SIMILAR_IMAGES'] + "/frame" + str(i) + ".jpg"), cv_img[i])
        
    # for idx, image in enumerate(similarImagesList):
    #     cv2.imwrite(os.path.join(app.config['SIMILAR_IMAGES'], "frame" + str(idx) + ".jpg"), image)
        
    return render_template('search.html')
    # remove dirs to replace manual deletions of images and videos


################################################ OUTPUT RESULT PAGE ####################################################
@app.route('/result')
def result():
    imageList = os.listdir(app.config['SIMILAR_IMAGES'])
    imageList = ["similarImages/" + image for image in imageList]
    shutil.make_archive("similar_images", 'zip', app.config['SIMILAR_IMAGES'])

    if(os.path.exists('./meta-data-files')):
        shutil.rmtree('./meta-data-files')
    # remove the dir uploadedImage 
    if(os.path.exists('./static/uploadedImage')):
        shutil.rmtree('./static/uploadedImage')
    # remove the dir uploadedVideo
    if(os.path.exists('./static/uploadedVideo')):
        shutil.rmtree('./static/uploadedVideo')
    # remove the dir extractedImages
    if(os.path.exists('./static/extractedImages')):
        shutil.rmtree('./static/extractedImages')

    # make a dir for uploaded video in case user returns to uploadedImage.html
    os.mkdir('./static/uploadedImage')

    return render_template('result.html', imageList=imageList)


# @app.route('choppedImages')
# def result():
#     return render_template('choppedImages.html')



################################################ RUN THE APPLICATION ####################################################
if __name__ == '__main__':
   app.run()
