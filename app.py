# import dependencies
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# import Flask
from flask import Flask, jsonify

# create function to access SQLite
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect the database
Base = automap_base()
Base.prepare(engine, reflect=True)

# create variables to reference each class
Measurement = Base.classes.measurement
Station = Base.classes.station

# create session link from python
session = Session(engine)

# define flask app
app = Flask(__name__)

# define main welcome route
@app.route("/")

# function to define all routes
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
