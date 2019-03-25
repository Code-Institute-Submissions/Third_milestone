import os, random
from flask import Flask, render_template, redirect, request, url_for, session, Response, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.json_util import dumps


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'surfingeurope'
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)

'''''''''''''''''''''''''''''''''
HELPER FUNCTIONS
'''''''''''''''''''''''''''''''''

def user_in_session():
    if 'username' in session:
        return session['username']
    else:
        return 'Log In'


'''''''''''''''''''''''''''''''''
INDEX
'''''''''''''''''''''''''''''''''

@app.route('/')
def index():

    '''
    Limit operator will display 3 top rated location
    '''

    locations = mongo.db.locations.aggregate([
        { '$unwind': '$ratings' },
        {
            '$group': {
                '_id': '$name',
                'average_rating': { '$avg': '$ratings.rate'},
                'country_name': { '$addToSet': '$country'},
                'break_type_name': { '$addToSet': '$break_type'},
                'old_id': { '$addToSet': '$_id'}
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
    Sample operator will display 3 random location including the top rated from above
    '''

    locations_random = mongo.db.locations.aggregate([
        { '$unwind': '$ratings' },
        { 
            '$group': {
                '_id': '$name',
                'average_rating': { '$avg': '$ratings.rate'},
                'country_name': { '$addToSet': '$country'},
                'break_type_name': { '$addToSet': '$break_type'},
                'old_id': { '$addToSet': '$_id'}
            }
        },
        { 
            '$sample': { 'size': 3 }
        },
        { 
            '$limit': 3 
        }
    ])
    user = user_in_session()
    return render_template('index.html', locations=locations, user=user, locations_random=locations_random)

'''''''''''''''''''''''''''''''''
ALL LOCATIONS WITH SORT FILTER
'''''''''''''''''''''''''''''''''

@app.route('/locations')
def locations():
    user = user_in_session()
    locations = mongo.db.locations.aggregate([
        { '$unwind': '$ratings' },
        {
            '$group': {
                '_id': '$name',
                'average_rating': { '$avg': '$ratings.rate'},
                'country_name': { '$addToSet': '$country'},
                'break_type_name': { '$addToSet': '$break_type'},
                'old_id': { '$addToSet': '$_id'}
            }
        },
        { 
            '$sort': { '_id': 1 }
        }
    ])

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
                'break_type_name': { '$addToSet': '$break_type'},
                'old_id': { '$addToSet': '$_id'}
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
                'break_type_name': { '$addToSet': '$break_type'},
                'old_id': { '$addToSet': '$_id'}
            }
        },
        { 
            '$sort': { 'average_rating': -1, '_id': 1 }
        }
    ])
    return render_template('locations.html',user=user, locations=locations)

'''''''''''''''''''''''''''''''''
SELECTED LOCATION
'''''''''''''''''''''''''''''''''

@app.route('/spot/<location_id>', methods=['POST', 'GET'])
def spot(location_id):
    user = user_in_session()
    location = mongo.db.locations.find_one({'_id': ObjectId(location_id)})
    locations_random = mongo.db.locations.aggregate([
        { '$unwind': '$ratings' },
        {
            '$group': {
                '_id': '$name',
                'average_rating': { '$avg': '$ratings.rate'},
                'country_name': { '$addToSet': '$country'},
                'break_type_name': { '$addToSet': '$break_type'},
                'old_id': { '$addToSet': '$_id'}
            }
        },
        { 
            '$sample': { 'size': 3 }
        },
        {
            '$limit': 3
        }
    ])

    return render_template('spot.html', user=user, location=location, locations_random=locations_random)

@app.route('/user_input/<location_id>', methods=['POST', 'GET'])
def user_input(location_id):
    user = user_in_session()
    location = mongo.db.locations.find_one({'_id': ObjectId(location_id)})
    if request.method == 'POST':
        mongo.db.locations.update(
            {
                '_id': ObjectId(location_id)
            },
            {
                '$push': {
                    'ratings': {
                        '$each': [ { 'user_name': user, 'rate': request.form['rating'] } ]
                    }
                }
            }
            # {
            #     '$addToSet': { 'ratings.rate': request.form['rating'] }
            # }
            # {
            #     '$push': {
            #         'ratings.user_name': user,
            #         'ratings.rate': request.form['rating'] 
            #     }
            # }
        )

    print(location)
    
    return render_template('user_input.html', user=user, location=location)

# @app.route('/rating/<location_id>', methods=['POST', 'GET'])
# def rating(location_id):
#     if request.method == 'POST':
#         if 'username' in session:
#             user = session['username']
#             location = mongo.db.locations.find_one({'_id': ObjectId(location_id)})
#             location.update({
#                 '$set': {
#                     'ratings': { 
#                         'user_name': user,
#                         'rate': request.form['rating'] 
#                         }
#                 }
#             })
#             return redirect(url_for('index'))
#         return 'Please log in to rate this location'
#         print(user)
#         print(location)
#     return redirect(url_for('locations'))   


'''''''''''''''''''''''''''''''''
RATING
'''''''''''''''''''''''''''''''''

# @app.route('/rating', methods=['POST', 'GET'])
# def rating():
#     locations = mongo.db.locations
#     if 'username' in session:
#         user = session['username']
#         return user
#     return 'Please log in to rate this location'
    
#     if request.method == 'POST':
#         if user:
#             locations.insert({'ratings': { 
#                 'user_name': user,
#                 'rate': request.form['rating'] 
#                 }
#             })
#             return redirect(url_for('/spot/<location_id>'))
#         return 'Please log in to rate this location'

'''''''''''''''''''''''''''''''''
SEARCH
'''''''''''''''''''''''''''''''''

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
    location_name = dumps(mongo.db.locations.find( {}, { '_id': 0, 'name': 1 } ))
    search_name = request.form.get('search_loc_name')

    if request.method == 'POST':
        print(request.form)
    return render_template('search.html', user=user, countries=countries, break_types=break_types, wave_directions=wave_directions, bottom=bottom, facilities=facilities, hazards=hazards, location_name=location_name)

'''''''''''''''''''''''''''''''''
ADD LOCATION
'''''''''''''''''''''''''''''''''

@app.route('/add_spot')
def add_spot():
    user = user_in_session()
    return render_template('addSpot.html', user=user, locations=mongo.db.locations.find())

'''''''''''''''''''''''''''''''''
ABOUT
'''''''''''''''''''''''''''''''''

@app.route('/about')
def about():
    user = user_in_session()
    return render_template('about.html', user=user, locations=mongo.db.locations.find())

'''''''''''''''''''''''''''''''''
LOG IN | LOG OUT and USER PAGE
'''''''''''''''''''''''''''''''''

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
    error = None
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})
        if existing_user is None:
            users.insert({'name' : request.form['username'] })
            session['username'] = request.form['username']
            flash('You were successfully registered ')
            return redirect(url_for('index'))
        error = 'That username already exists!'
    return render_template('register.html', error=error)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT', '5000')),
    debug=True)