import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'surfingeurope'
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


def get_locations():
    locations = mongo.db.locations.find()
    return locations

def get_facilities():
    facilities = mongo.db.categories.find( { 'facilities': { '$eq': ["parking", "accommodation", "food", "bar", "showers", "toilets", "school & rental"] } } )
    return facilities

def get_location_name():
    location_name = mongo.db.locations.find( { 'name': { '$ne': 'null' }} )
    return location_name


@app.route('/')
def index():
    locations = get_locations()
    facilities = get_facilities()
    location_name = get_location_name()
    return render_template('index.html', locations=locations, facilities=facilities, location_name=location_name)

@app.route('/locations')
def locations():
    return render_template('locations.html', locations=mongo.db.locations.find())

@app.route('/search')
def search():
    categories = mongo.db.categories
    countries = categories.find( { 'country': {'$ne': 'null'} } )
    break_types = categories.find( { 'break_type': {'$ne': 'null'} } )
    wave_directions = categories.find( { 'wave_direction': {'$ne': 'null'} } )
    bottom = categories.find( { 'bottom': {'$ne': 'null'} } )
    facilities = categories.find( { 'facilities': {'$ne': 'null'} } )
    hazards = categories.find( { 'hazards': {'$ne': 'null'} } )
    return render_template('search.html', countries=countries, break_types=break_types, wave_directions=wave_directions, bottom=bottom, facilities=facilities, hazards=hazards)

@app.route('/add_spot')
def add_spot():
    return render_template('addSpot.html', locations=mongo.db.locations.find())

@app.route('/about')
def about():
    return render_template('about.html', locations=mongo.db.locations.find())

@app.route('/register')
def register():
    return render_template('register.html', locations=mongo.db.locations.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT', '5000')),
    debug=True)