from flask import Flask, render_template, redirect, url_for, request, abort, send_from_directory
import imghdr
import os
from werkzeug.utils import secure_filename
import deepImageSearch
from os import getcwd
from datetime import datetime
import cv2


app = Flask(__name__)

# Config for extensions for video and images
app.config['PHOTO_EXTENSIONS'] = ['.jpg', '.png', '.jpeg']
app.config['VIDEO_EXTENSIONS'] = ['.mp4']

# Config for uploaded images/videos path
app.config['UPLOAD_PATH_IMAGE'] = './static/uploadedImage'
app.config['UPLOAD_PATH_VIDEO'] = './static/uploadedVideo'

# Config for extracted images from video
app.config['EXTRACTED_IMAGES'] = './static/extractedImages'


################################################ LOGIN PAGE ####################################################
# First rendered papge
@app.route('/')
def home():
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
    return redirect(url_for('loading'))

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
@app.route('/loading')
def loading():
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
    videoName = os.listdir(app.config['UPLOAD_PATH_VIDEO'])[0]
    videoFile = os.path.join(app.config['UPLOAD_PATH_VIDEO'], videoName)
    extractImages(videoFile)
    redirect(url_for('result'))
    return render_template('loading.html')



################################################ OUTPUT RESULT PAGE ####################################################
@app.route('/result')
def result():
   resultArray = deepImageSearch.imageSearch()
   
   return render_template('result.html')







################################################ RUN THE APPLICATION ####################################################
if __name__ == '__main__':
   app.run()
