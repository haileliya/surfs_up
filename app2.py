import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()

#Add the following code to reflect the database:
Base.prepare(engine, reflect=True)

#save our references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#create a session link from Python to our database
session = Session(engine)

#create a Flask application called "app."
app = Flask(__name__)

#welcome route using the code 
@app.route("/")

#dd the routing information for each of the other routes. For this we'll create a function, 
#and our return statement will have f-strings as a reference to all of the other routes

#create a function welcome() with a return statement
def welcome():
    return
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
#add the precipitation, stations, tobs, and temp routes 
#that we'll need for this module into our return statement. We'll use f-strings to display them 

flask run
