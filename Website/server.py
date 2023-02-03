from flask import Flask, render_template, redirect, url_for, request, abort, send_from_directory
import imghdr
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['PHOTO_EXTENSIONS'] = ['.jpg', '.png', '.jpeg']
app.config['VIDEO_EXTENSIONS'] = ['.mp4']
app.config['UPLOAD_PATH'] = './static/uploads'

@app.route('/')
def home():
   return render_template('login.html')

@app.route('/', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
      if request.form['username'] != 'RosenA' or request.form['password'] != 'RosenA':
         return home()
      else:
         return redirect(url_for('index'))

@app.route('/index')
def index():
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('index.html', files=files)

@app.route('/index', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['PHOTO_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    return redirect(url_for('index'))

@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)

@app.route('/index2')
def index2():
   files = os.listdir(app.config['UPLOAD_PATH'])
   return render_template('index2.html')

@app.route('/index2', methods=['POST'])
def upload_video():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['VIDEO_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    return redirect(url_for('index2'))

@app.route('/image')
def image():
   return render_template('image.html')

@app.route('/frames')
def frames():
   return render_template('frames.html')

@app.route('/result')
def result():
   return render_template('result.html')

if __name__ == '__main__':
   app.run()
