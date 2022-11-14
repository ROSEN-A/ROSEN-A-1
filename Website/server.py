from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/image')
def image():
   return render_template('image.html')

@app.route('/index')
def index():
   return home()


if __name__ == '__main__':
   app.run()