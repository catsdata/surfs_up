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
    Welcome to the Climate Analysis API!<br/>
    Available Routes:<br/>
    /api/v1.0/precipitation<br/>
    /api/v1.0/stations<br/>
    /api/v1.0/tobs<br/>
    /api/v1.0/temp/start/end
    ''')

# create route to precip
@app.route("/api/v1.0/precipitation")

# create precip function
def precipitation():

    # calculate date and precip from a year ago
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
    # create a dictionary with the date as the key and the precipitation as the value
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# create route to stations
@app.route("/api/v1.0/stations")

# create precip function
def stations():
    
    # create query to get all stations 
    results = session.query(Station.station).all()
    
    # unravel results into one dim array with results as parameter
    stations = list(np.ravel(results))
    
    # convert results into json list
    return jsonify(stations=stations)    

# create route to temp observations
@app.route("/api/v1.0/tobs")

# create temp function
def temp_monthly():
    
    # calc one year ago
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    # query all temps from last year
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    
    # unravel into one dimensional array
    temps = list(np.ravel(results))
    
    # convert results into json list
    return jsonify(temps=temps)

# create route to stats with start and end dates
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# create stats function with start and end parameters
def stats(start=None, end=None):
    
    # create query list from sqlite for max, min, avg
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    # determine start/end dates, unravel into json; asterisk indicates multiple results
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)
    
    # calculate temp stats with dates using sel list & unravel
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)   









