import os, random
from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for, session, Response, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.json_util import dumps


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'surfingeurope'
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)

"""
HELPER FUNCTIONS
"""

def user_in_session():
    if 'username' in session:
        return session['username']

def facilities_to_Array(advanced_search_results):
    checkbox_results = []
    for key, value in advanced_search_results.items():
        if value == 'include':
            checkbox_results.append(key)
    if checkbox_results == []:
        return {'$exists': 'True'}
    return { '$all': checkbox_results }

def hazards_to_Array(advanced_search_results):
    checkbox_results = []
    for key, value in advanced_search_results.items():
        if value == 'exclude':
            checkbox_results.append(key)
    if checkbox_results == []:
        return {'$exists': 'True'}
    return { '$nin': checkbox_results }


"""
INDEX
"""

@app.route('/')
def index():

    '''
    Limit operator will display 3 top rated location
    '''

    locations = mongo.db.locations.aggregate([
        { '$unwind': '$ratings' },
        { '$group': {
            '_id': '$name',
            'average_rating': { '$avg': '$ratings.rate'},
            'country_name': { '$addToSet': '$country'},
            'break_type_name': { '$addToSet': '$break_type'},
            'old_id': { '$addToSet': '$_id'}
            } },
        { '$sort': { 'average_rating': -1, '_id': 1 } },
        { '$limit': 3 }
    ])
    
    '''
    Sample operator will display 3 random location including the top rated from above
    '''

    locations_random = mongo.db.locations.aggregate([
        { '$unwind': '$ratings' },
        { '$group': {
            '_id': '$name',
            'average_rating': { '$avg': '$ratings.rate'},
            'country_name': { '$addToSet': '$country'},
            'break_type_name': { '$addToSet': '$break_type'},
            'old_id': { '$addToSet': '$_id'}
            } },
        { '$sample': { 'size': 3 } },
        { '$limit': 3 }
    ])
    user = user_in_session()
    return render_template('index.html', locations=locations, user=user, locations_random=locations_random)

"""
ALL LOCATIONS WITH SORT FILTER
"""

@app.route('/locations')
def locations():
    user = user_in_session()
    locations = mongo.db.locations.aggregate([
        { '$unwind': '$ratings' },
        { '$group': {
            '_id': '$name',
            'average_rating': { '$avg': '$ratings.rate'},
            'country_name': { '$addToSet': '$country'},
            'break_type_name': { '$addToSet': '$break_type'},
            'old_id': { '$addToSet': '$_id'}
            } },
        { '$sort': { '_id': 1 } }
    ])
    return render_template('locations.html',user=user, locations=locations)


@app.route('/locations_by_country')
def locations_by_country():
    user = user_in_session()
    locations = mongo.db.locations.aggregate([
        { '$unwind': '$ratings' },
        { '$group': {
            '_id': '$name',
            'average_rating': { '$avg': '$ratings.rate'},
            'country_name': { '$addToSet': '$country'},
            'break_type_name': { '$addToSet': '$break_type'},
            'old_id': { '$addToSet': '$_id'}
            } },
        { '$sort': { 'country_name': 1, '_id': 1 } }
    ])
    return render_template('locations.html',user=user, locations=locations)


@app.route('/locations_by_rating')
def locations_by_rating():
    user = user_in_session()
    locations = mongo.db.locations.aggregate([
        { '$unwind': '$ratings' },
        { '$group': {
            '_id': '$name',
            'average_rating': { '$avg': '$ratings.rate'},
            'country_name': { '$addToSet': '$country'},
            'break_type_name': { '$addToSet': '$break_type'},
            'old_id': { '$addToSet': '$_id'}
            } },
        { '$sort': { 'average_rating': -1, '_id': 1 } }
    ])
    return render_template('locations.html',user=user, locations=locations)

"""
SELECTED LOCATION
"""

@app.route('/spot/<location_id>', methods=['POST', 'GET'])
def spot(location_id):
    user = user_in_session()
    if 'username' not in session:
        flash('Please log in to rate and comment on this location', 'login')
    else:
        flash('Please comment and rate this location below:', 'login')
    location = mongo.db.locations.find_one({'_id': ObjectId(location_id)})
    avg_rating = mongo.db.locations.aggregate([
        { '$match': {
            '_id': ObjectId(location_id)
            } },
        { '$unwind': '$ratings' },
        { '$group': {
            '_id': '$name',
            'average_rating': { '$avg': '$ratings.rate'},
            'country_name': { '$addToSet': '$country'},
            'break_type_name': { '$addToSet': '$break_type'},
            'old_id': { '$addToSet': '$_id'}
            } }
    ])
    locations_random = mongo.db.locations.aggregate([
        { '$unwind': '$ratings' },
        { '$group': {
            '_id': '$name',
            'average_rating': { '$avg': '$ratings.rate'},
            'country_name': { '$addToSet': '$country'},
            'break_type_name': { '$addToSet': '$break_type'},
            'old_id': { '$addToSet': '$_id'}
            } },
        { '$sample': { 'size': 3 } },
        { '$limit': 3 }
    ])

    return render_template('spot.html', user=user, location=location, avg_rating=avg_rating, locations_random=locations_random)

"""
RATES AND COMMENTS
"""

@app.route('/user_input/<location_id>', methods=['POST', 'GET'])
def user_input(location_id):
    user = user_in_session()
    user_in_rating = None

    if mongo.db.locations.find({ 'ratings.user_name': user }):
        user_in_rating = user

    now = datetime.now().strftime('%Y-%m-%d at %H:%M:%S')
    location = mongo.db.locations.find_one({'_id': ObjectId(location_id)})
    
    if 'username' not in session:
        flash('Please log in or register to rate and comment!')
        return redirect(url_for('user'))

    if request.method == 'POST':
        if 'rating' in request.form:
            mongo.db.locations.update(
                { '_id': ObjectId(location_id), 'ratings.user_name': user },
                { '$set': { 'ratings.$.rate': request.form.get('rating', type=int) } },
                False, True
            )
            mongo.db.locations.update(
                { '_id': ObjectId(location_id), 'ratings.user_name': { '$ne': user } },
                { '$addToSet': { 
                    'ratings': { 
                        'user_name': user, 'rate': request.form.get('rating', type=int) } } },
                False, True
            )
            flash('Thank you for your rating!', 'spot')
            return redirect(url_for('spot', location_id=location_id))
        else:
            mongo.db.locations.update(
            { '_id': ObjectId(location_id) },
            { '$push': {
                'comments': {
                    '$each': [ { 
                        'user_name': user, 'date_added': now, 'comment': request.form['add_comment'] } ] }
                }
            }
        )
        flash('Thank you for your comment!', 'spot')
        return redirect(url_for('spot', location_id=location_id))

    return render_template('user_input.html', user=user, location=location)

"""
SEARCH
"""

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

    return render_template('search.html', user=user, countries=countries, break_types=break_types, wave_directions=wave_directions, bottom=bottom, facilities=facilities, hazards=hazards, location_name=location_name)


@app.route('/search_by_name', methods=['POST'])
def search_by_name():
    user = user_in_session()
    categories = mongo.db.categories
    countries = categories.find( { 'country': {'$ne': 'null'} } )
    break_types = categories.find( { 'break_type': {'$ne': 'null'} } )
    wave_directions = categories.find( { 'wave_direction': {'$ne': 'null'} } )
    bottom = categories.find( { 'bottom': {'$ne': 'null'} } )
    facilities = categories.find( { 'facilities': {'$ne': 'null'} } )
    hazards = categories.find( { 'hazards': {'$ne': 'null'} } )

    search_result = mongo.db.locations.find_one({'name' : request.form['search_by_name']})
    if search_result == None:
        return redirect(url_for('oups'))
    name_search = mongo.db.locations.aggregate([
        { '$match': {'name' : search_result['name'] } },
        { '$unwind': '$ratings' },
        { '$group': {
                '_id': '$name',
                'average_rating': { '$avg': '$ratings.rate'},
                'country_name': { '$addToSet': '$country'},
                'break_type_name': { '$addToSet': '$break_type'},
                'old_id': { '$addToSet': '$_id'}
            } },
        { '$sort': { '_id': 1 } }
    ])

    name_search = list(name_search)
    # print(name_search)

    return render_template('search.html', user=user, countries=countries, break_types=break_types, wave_directions=wave_directions, bottom=bottom, facilities=facilities, hazards=hazards, name_search=name_search)

@app.route('/advanced_search', methods=['POST'])
def advanced_search():
    user = user_in_session()
    categories = mongo.db.categories
    countries = categories.find( { 'country': {'$ne': 'null'} } )
    break_types = categories.find( { 'break_type': {'$ne': 'null'} } )
    wave_directions = categories.find( { 'wave_direction': {'$ne': 'null'} } )
    bottom = categories.find( { 'bottom': {'$ne': 'null'} } )
    facilities = categories.find( { 'facilities': {'$ne': 'null'} } )
    hazards = categories.find( { 'hazards': {'$ne': 'null'} } )

    advanced_search_results = request.form.to_dict()
    del advanced_search_results['action']

    country_in = request.form.get('country_selection')
    country_out = {'$exists': 'True'}
    break_type_in = request.form.get('break_type_selection')
    break_type_out = {'$exists': 'True'}
    wave_direction_in = request.form.get('wave_direction_selection')
    wave_direction_out = {'$exists': 'True'}
    bottom_type_in = request.form.get('bottom_selection')
    bottom_type_out = {'$exists': 'True'}

    if 'country_selection' in request.form:
        country = country_in
    else:
        country = country_out
    
    if 'break_type_selection' in request.form:
        break_type = break_type_in
    else:
        break_type = break_type_out

    if 'wave_direction_selection' in request.form:
        wave_direction = wave_direction_in
    else:
        wave_direction = wave_direction_out

    if 'bottom_selection' in request.form:
        bottom_type = bottom_type_in
    else:
        bottom_type = bottom_type_out

    adv_search = mongo.db.locations.aggregate([
        { '$match': { '$and': [ { 
        'country': country,
        'break_type': break_type,
        'wave_direction': wave_direction,
        'bottom': bottom_type,
        'hazards': hazards_to_Array(advanced_search_results),
        'facilities': facilities_to_Array(advanced_search_results)
        } ]
        }
    },
    { '$unwind': '$ratings' },
    { '$group': {
        '_id': '$name',
        'average_rating': { '$avg': '$ratings.rate'},
        'country_name': { '$addToSet': '$country'},
        'break_type_name': { '$addToSet': '$break_type'},
        'old_id': { '$addToSet': '$_id'}
        } },
    { '$sort': { 'average_rating': -1, '_id': 1 } }
    ])

    adv_search = list(adv_search)

    if adv_search == []:
        return redirect(url_for('oups'))
    
    return render_template('search.html', user=user, countries=countries, break_types=break_types, wave_directions=wave_directions, bottom=bottom, facilities=facilities, hazards=hazards, adv_search=adv_search)


@app.route('/oups')
def oups():
    error = 'Your search did not match any of our records. Please refine your search or if you believe we are missing this location, please add it to our collection!'
    return render_template('oups.html', error=error)



"""
ADD LOCATION
"""

@app.route('/add_spot')
def add_spot():
    user = user_in_session()
    return render_template('addSpot.html', user=user, locations=mongo.db.locations.find())

"""
ABOUT
"""

@app.route('/about')
def about():
    user = user_in_session()
    return render_template('about.html', user=user, locations=mongo.db.locations.find())

"""
LOG IN | LOG OUT and USER PAGE
"""

@app.route('/login', methods=['POST'])
def login():
    error = None
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
        session['username'] = request.form['username']
        flash('Welcome back!')
        return redirect(url_for('user_logged'))
    error = 'Looks like invalid username. Please try to type again or register below'
    return render_template('user.html', error=error)


@app.route('/user')
def user():
    user = user_in_session()
    return render_template('user.html', user=user)


@app.route('/user_logged')
def user_logged():
    user = user_in_session()
    # xxx = mongo.db.locations.aggregate([
    #     { '$match': { 'ratings.name': user } },
        
    # ])
    locations_user = mongo.db.locations.find({
        # { '$match': {
        #     '_id': ObjectId(location_id)
        #     }
        # },
        '$or': [
            { 'ratings.user_name': user },
            { 'comments.user_name': user }
            ]
        })
    test = mongo.db.locations.aggregate([
        # {
        #     '$group': {
        #         '_id': '$_id',
        #         'name': { '$addToSet': '$name'},
        #         'user_name': { '$addToSet': '$ratings.user_name'},
        #         'rate': { '$addToSet': '$ratings.rate'},
        #     }
        # },
        {
            '$project': {
                'ratings': {
                    '$filter': {
                        'input': '$ratings',
                        'as': 'rate',
                        'cond': {
                            '$eq': [ '$$rate.user_name', user ]
                        }
                    }
                }
            }
        }
    ]
    )
    # print(list(locations_user))
    # loc = mongo.db.locations.aggregate([
    #     { '$match': {
    #         'ratings.user_name': user
    #         }
    #     },
    #     { '$unwind': '$ratings' },
    #     {
    #         '$group': {
    #             '_id': '$name',
    #             'average_rating': { '$avg': '$ratings.rate'},
    #             'user_rate': { '$addToSet': '$ratings.rate'},
    #             'user_name': { '$addToSet': '$ratings.user_name'},
    #             'country_name': { '$addToSet': '$country'},
    #             'break_type_name': { '$addToSet': '$break_type'},
    #             'old_id': { '$addToSet': '$_id'}
    #         }
    #     }
    # ])
    return render_template('user_logged.html', user=user, locations=locations, locations_user=locations_user, test=test)


@app.route('/user_logout')
def user_logout():
    session.clear()
    return redirect(url_for('index'))

"""
REGISTER
"""

@app.route('/register', methods=['POST', 'GET'])
def register():
    error = None
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})
        if existing_user is None:
            users.insert({'name' : request.form['username'] })
            session['username'] = request.form['username']
            flash('You were successfully registered!')
            return redirect(url_for('user_logged'))
        error = 'That username already exists. Please choose another one.'
    return render_template('register.html', error=error)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT', '5000')),
    debug=True)