from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

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
   return render_template('index.html')

@app.route('/image')
def image():
   return render_template('image.html')

@app.route('/result')
def result():
   return render_template('result.html')

if __name__ == '__main__':
   app.run()