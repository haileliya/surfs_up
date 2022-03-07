from flask import Flask

#create a new Flask instance called app
app = Flask(__name__)

#First, we need to define the starting point, also known as the root. To do this, we'll use the function @app.route('/')
@app.route('/')
#forward slash inside of the app.route? This denotes that we want to put our data at the root of our routes. 
#The forward slash is commonly known as the highest level of hierarchy in any computer system.

@app.route('/')
def hello_world():
    return 'Hello world'

export FLASK_APP=app.py
