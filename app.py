import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.json_util import dumps


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'surfingeurope'
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = 'super secret key'

mongo = PyMongo(app)


def get_locations():
    locations = mongo.db.locations.find()
    return locations

def get_facilities():
    facilities = mongo.db.categories.find( { 'facilities': { '$eq': ["parking", "accommodation", "food", "bar", "showers", "toilets", "school & rental"] } } )
    return facilities

def get_locations_name():
    # location_name = mongo.db.locations.find( { 'name': { '$ne': 'null' }} )
    location_name = dumps(mongo.db.locations.find( {}, { '_id': 0, 'name': 1 } ))
    return location_name

def users_loged():
    if 'username' in session:
        return session['username']
    else:
        return ''

@app.route('/')
def index():
    
    locations = get_locations()
    facilities = get_facilities()
    user = users_loged()
    return render_template('index.html', locations=locations, facilities=facilities, user=user, location_name=get_locations_name())

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

    search_name = request.form.get('search_loc_name')

    if request.method == 'POST':
        print(request.form)
    return render_template('search.html', countries=countries, break_types=break_types, wave_directions=wave_directions, bottom=bottom, facilities=facilities, hazards=hazards, location_name=get_locations_name())

@app.route('/add_spot')
def add_spot():
    return render_template('addSpot.html', locations=mongo.db.locations.find())

@app.route('/about')
def about():
    return render_template('about.html', locations=mongo.db.locations.find())

@app.route('/user')
def user():
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return render_template('user.html')

@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
        session['username'] = request.form['username']
        return redirect(url_for('index'))

    return 'Invalid username'

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            users.insert({'name' : request.form['username']})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        return 'That username already exists!'

    return render_template('register.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT', '5000')),
    debug=True)