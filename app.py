import datetime as dt
import json
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#Set Up the Database
engine = create_engine("sqlite:///hawaii.sqlite")

#THIS LINE OF CODE ALLOWS ME TO ACCESS THE SQLITE DATABASE SO THAT WE CAN QUERY OUR FILE.

# NOW ITS TIME TO REFLECT/COPY OUR DATABASE INTO CLASSES
Base = automap_base()
# THIS LINE OF CODE REFLECTS THE DATABASE
Base.prepare(engine, reflect=True)

#With the database reflected, we can save our references to each table. Again, they'll be the same references as the ones we wrote earlier 
#in this module. We'll create a variable for each of the classes so that we can reference them later, as shown below.

Measurement = Base.classes.measurement
Station = Base.classes.station

#Finally, create a session link from Python to our database with the following code:

session = Session(engine)

app = Flask(__name__)
# FIRST ROUTE
@app.route("/")
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


#Every time you create a new route, your code should be aligned to the left in order to avoid errors.

#To create the route, add the following code. Make sure that it's aligned all the way to the left.
#Next, we will create the precipitation() function.
#First, we want to add the line of code that calculates the date one year ago from the most recent
# date in the database. Do this now so that your code looks like the following:
#Next, write a query to get the date and precipitation for the previous year. 
# Add this query to your existing code.

# SECOND ROUTE
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
     filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)



# Finally, we'll create a dictionary with the date as the key and the precipitation as the value. 
# To do this, we will "jsonify" our dictionary. Jsonify() is a function that converts the dictionary 
# to a JSON file.

# THIRD ROUTE
#Now we need to create a query that will allow us to get all of the stations in our database. 
# Let's add that functionality to our code:
#We want to start by unraveling our results into a one-dimensional array. To do this, we want to use the function np.ravel(), with results as our parameter.
#Next, we will convert our unraveled results into a list. To convert the results to a list, we will 
# need to use the list function, which is list(), and then convert that array into a list. 
# Then we'll jsonify the list and return it as JSON. Let's add that functionality to our code:


@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)


# FOURTH ROUTE
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)


# LAST ROUTES
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)


    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)
