import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import func

from flask import Flask, jsonify, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL', '') or "sqlite:///db/data.sqlite"
db = SQLAlchemy(app)

# reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(db.engine, reflect=True)

# # Save references to each table
# # Samples_Metadata = Base.classes.sample_metadata
# Samples = Base.classes.samples

# Create our database model
class Samples(db.Model):
    __tablename__ = 'samples'

    index = db.Column(db.Integer, primary_key=True)
    Price = db.Column(db.Integer)
    Year = db.Column(db.String)
    Mileage = db.Column(db.Integer)
    City = db.Column(db.String)
    State = db.Column(db.String)
    Vin = db.Column(db.String)
    sample = db.Column(db.String)
    MSRP = db.Column(db.Integer)
    Latitude = db.Column(db.Float)
    Longitude = db.Column(db.Float)
    Model = db.Column(db.String)
    Depreciation = db.Column(db.Float)

    def __repr__(self):
        return '<Samples %r>' % (self.name)


# Create database tables
@app.before_first_request
def setup():
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()


@app.route("/")
def index():
    """Return the homepage."""

    return render_template("index.html")

@app.route("/makes/")
def makes():
    """Return the homepage."""

    return render_template("makes.html")

@app.route("/plot/")
def plot():
    """Return the homepage."""

    return render_template("plot.html")


@app.route("/names")
def names():
    """Return a list of sample names."""

    # Use Pandas to perform the sql query
    stmt = db.session.query(Samples).group_by(Samples.sample).statement
    df = pd.read_sql_query(stmt, db.session.bind)
    make_data = df['sample']
    # Return a list of the column names (sample names)
    return jsonify(make_data.tolist())


@app.route("/samples/<sample>")
def samples(sample):
    """Return data for a given sample."""
    sel = [
        Samples.sample,
        Samples.Price,
        Samples.Year,
        Samples.Mileage,
        Samples.Latitude,
        Samples.Longitude,
        Samples.City,
        Samples.MSRP,
        Samples.Depreciation
    ]


    stmt = db.session.query(*sel).filter(Samples.sample == sample).statement
    df = pd.read_sql_query(stmt, db.session.bind)


    data = {
        'sample': df['sample'].tolist(),
        'Price': df['Price'].tolist(),
        'Year': df['Year'].tolist(),
        'Mileage': df['Mileage'].tolist(),
        'Latitude': df['Latitude'].tolist(),
        'Longitude': df['Longitude'].tolist(),
        'City': df['City'].tolist(),
        'MSRP': df['MSRP'].tolist(),
        'Depreciation': df['Depreciation'].tolist(),
        }

    return jsonify(data)

@app.route("/average")
def average():

    results = db.session.query(Samples.sample, func.avg(Samples.Price), func.avg(Samples.MSRP)).group_by(Samples.sample).all()

    vehicles = []
    for sample, Price, MSRP in results:
        vehicle_dict = {}
        vehicle_dict['sample'] = sample
        vehicle_dict['Price'] = Price
        vehicle_dict['MSRP'] = MSRP
        vehicles.append(vehicle_dict)
    return jsonify(vehicles)

@app.route("/chart")
def chart():

    results = db.session.query(Samples.Depreciation, Samples.Mileage).all()
    Depreciation = [result[0] for result in results]
    Mileage = [result[1] for result in results]
    Depreciation.insert(0, "Depreciation")
    Mileage.insert(0, "Mileage")
    data = {
        "Depreciation": Depreciation,
        "Mileage": Mileage,
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run()