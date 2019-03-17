import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'surfingeurope'
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html', categories=mongo.db.categories.find(), locations=mongo.db.locations.find())

@app.route('/locations')
def locations():
    return render_template('locations.html', locations=mongo.db.locations.find())

@app.route('/search')
def search():
    return render_template('search.html', locations=mongo.db.locations.find())

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