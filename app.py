import os, random
from flask import Flask, render_template, redirect, request, url_for, session, Response
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.json_util import dumps


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'surfingeurope'
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = 'super secret key'

mongo = PyMongo(app)

'''
HELPER FUNCTIONS
'''

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

def user_in_session():
    if 'username' in session:
        return session['username']
    else:
        return 'Log In'


'''
INDEX
'''

@app.route('/')
def index():

    '''
    locations will show 3 top rated location
    '''

    locations = mongo.db.locations.aggregate([
        { '$unwind': '$ratings' },
        {
            '$group': {
                '_id': '$name',
                'average_rating': { '$avg': '$ratings.rate'},
                'country_name': { '$addToSet': '$country'},
                'break_type_name': { '$addToSet': '$break_type'}
            }
        },
        { 
            '$sort': { 'average_rating': -1, '_id': 1 }
        },
        { 
            '$limit': 3
        }
    ])

    '''
    Ranodm selection will display 3 random location including the top rated from above
    '''

    locations_random = mongo.db.locations.aggregate([
        { '$unwind': '$ratings' },
        {
            '$group': {
                '_id': '$name',
                'average_rating': { '$avg': '$ratings.rate'},
                'country_name': { '$addToSet': '$country'},
                'break_type_name': { '$addToSet': '$break_type'}
            }
        },
        { 
            '$sample': { 'size': 3 }
        },
        {
            '$limit': 3
        }
    ])
    facilities = get_facilities()
    user = user_in_session()
    # random = mongo.db.locations.aggregate([{ '$sample': { 'size': 3 } }])
    return render_template('index.html', locations=locations, facilities=facilities, user=user, locations_random=locations_random)

'''
ALL LOCATIONS WITH SORT FILTER
'''

@app.route('/locations', methods=['GET', 'POST'])
def locations():
    user = user_in_session()
    locations = mongo.db.locations.aggregate([
        { '$unwind': '$ratings' },
        {
            '$group': {
                '_id': '$name',
                'average_rating': { '$avg': '$ratings.rate'},
                'country_name': { '$addToSet': '$country'},
                'break_type_name': { '$addToSet': '$break_type'}
            }
        },
        { 
            '$sort': { '_id': 1 }
        }
    ])
    users = mongo.db.users.find()
    
    return render_template('locations.html',user=user, locations=locations)

@app.route('/locations_by_country')
def locations_by_country():
    user = user_in_session()
    locations = mongo.db.locations.aggregate([
        { '$unwind': '$ratings' },
        {
            '$group': {
                '_id': '$name',
                'average_rating': { '$avg': '$ratings.rate'},
                'country_name': { '$addToSet': '$country'},
                'break_type_name': { '$addToSet': '$break_type'}
            }
        },
        { 
            '$sort': { 'country_name': 1, '_id': 1 }
        }
    ])
    return render_template('locations.html',user=user, locations=locations)

@app.route('/locations_by_rating')
def locations_by_rating():
    user = user_in_session()
    locations = mongo.db.locations.aggregate([
        { '$unwind': '$ratings' },
        {
            '$group': {
                '_id': '$name',
                'average_rating': { '$avg': '$ratings.rate'},
                'country_name': { '$addToSet': '$country'},
                'break_type_name': { '$addToSet': '$break_type'}
            }
        },
        { 
            '$sort': { 'average_rating': -1, '_id': 1 }
        }
    ])
    return render_template('locations.html',user=user, locations=locations)

'''
SELECTED LOCATION
'''

@app.route('/spot/<location_id>')
def spot(location_id):
    user = user_in_session()
    location = mongo.db.locations.find_one({'_id': ObjectId(location_id)})
    random = mongo.db.locations.aggregate([{ '$sample': { 'size': 3 } }])
    return render_template('spot.html', user=user, location=location, random=random)

'''
SEARCH
'''

@app.route('/search')
def search():
    user = user_in_session()
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
    return render_template('search.html', user=user, countries=countries, break_types=break_types, wave_directions=wave_directions, bottom=bottom, facilities=facilities, hazards=hazards, location_name=get_locations_name())

'''
ADD LOCATION
'''

@app.route('/add_spot')
def add_spot():
    user = user_in_session()
    return render_template('addSpot.html', user=user, locations=mongo.db.locations.find())

'''
ABOUT
'''

@app.route('/about')
def about():
    user = user_in_session()
    return render_template('about.html', user=user, locations=mongo.db.locations.find())

'''
LOG IN | LOG OUT and USER PAGE
'''

@app.route('/user')
def user():
    user = user_in_session()
    return render_template('user.html', user=user)

@app.route('/user_logged')
def user_logged():
    user = user_in_session()
    return render_template('user_logged.html', user=user)

@app.route('/user_logout')
def user_logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
        session['username'] = request.form['username']
        return redirect(url_for('user_logged'))

    return 'Invalid username'

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            users.insert({'name' : { '$toLower': request.form['username'] }})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        return 'That username already exists!'

    return render_template('register.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT', '5000')),
    debug=True)