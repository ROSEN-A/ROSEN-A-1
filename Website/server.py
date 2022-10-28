from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')
if __name__ == '__main__':
   app.run()

# from flask import Flask
# from flask_mako import MakoTemplates, render_template

# app = Flask(__name__)
# mako = MakoTemplates(app)
# def sample():
#     return render_template("mako.html")

# if __name__ == '__main__':
#     app.run()