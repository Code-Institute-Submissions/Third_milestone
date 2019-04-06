import os, math
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

locations_db = mongo.db.locations
categories_db = mongo.db.categories

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

def facilities_to_new(input_location):
    checkbox_results = []
    for key, value in input_location.items():
        if value == 'facility':
            checkbox_results.append(key)
    return checkbox_results

def hazards_to_new(input_location):
    checkbox_results = []
    for key, value in input_location.items():
        if value == 'hazard':
            checkbox_results.append(key)
    return checkbox_results

def sort_locations(sort_by):
    sort_locations = ''
    if sort_by == 'rate':
        sort_locations = { 'average_rating': -1, '_id': 1 }
        return sort_locations
    elif sort_by == 'country':
        sort_locations = { 'country_name': 1, '_id': 1 }
        return sort_locations
    elif sort_by == 'name':
        sort_locations = { '_id': 1 }
        return sort_locations

"""
INDEX
"""

@app.route('/')
def index():

    '''
    Limit operator will display 3 top rated location
    '''

    locations = locations_db.aggregate([
        { '$unwind': '$ratings' },
        { '$group': {
            '_id': '$name',
            'average_rating': { '$avg': '$ratings.rate'},
            'country_name': { '$addToSet': '$country'},
            'break_type_name': { '$addToSet': '$break_type'},
            'old_id': { '$addToSet': '$_id'},
            'img_url': { '$addToSet': '$img_url'}
            } },
        { '$sort': { 'average_rating': -1, '_id': 1 } },
        { '$limit': 3 }
    ])
    
    '''
    Sample operator will display 3 random location including the top rated from above
    '''

    locations_random = locations_db.aggregate([
        { '$unwind': '$ratings' },
        { '$group': {
            '_id': '$name',
            'average_rating': { '$avg': '$ratings.rate'},
            'country_name': { '$addToSet': '$country'},
            'break_type_name': { '$addToSet': '$break_type'},
            'old_id': { '$addToSet': '$_id'},
            'img_url': { '$addToSet': '$img_url'}
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

    sort_by = request.args.get('sort_by', 'name')
    filters = ('name', 'country', 'rate')

    page = int(request.args.get('page', 1))
    print(page)
    page_limit = 6
    page_skip = page_limit * (page - 1)
    documents_number = locations_db.count()
    page_range = range(1, math.ceil(documents_number / page_limit) + 1)

    locations = locations_db.aggregate([
        { '$unwind': '$ratings' },
        { '$group': {
            '_id': '$name',
            'average_rating': { '$avg': '$ratings.rate'},
            'country_name': { '$addToSet': '$country'},
            'break_type_name': { '$addToSet': '$break_type'},
            'old_id': { '$addToSet': '$_id'},
            'img_url': { '$addToSet': '$img_url'}
            } },
        { '$sort': sort_locations(sort_by) },
        { '$skip': page_skip },
        { '$limit': page_limit }
    ])
    # print(locations)
    return render_template('locations.html',user=user, locations=locations, page=page, page_range=page_range, sort_by=sort_by, filters=filters)


"""
SELECTED LOCATION
"""

@app.route('/spot/<location_id>', methods=['POST', 'GET'])
def spot(location_id):
    user = user_in_session()
    if 'username' not in session:
        flash('Please log in to rate, comment ore edit this location', 'login')
    else:
        flash('Please leave your comment and rate this location. If you believe it needs to be updated please use the edit button. Thanks!', 'login')
    location = locations_db.find_one({'_id': ObjectId(location_id)})
    avg_rating = locations_db.aggregate([
        { '$match': {
            '_id': ObjectId(location_id)
            } },
        { '$unwind': '$ratings' },
        { '$group': {
            '_id': '$name',
            'average_rating': { '$avg': '$ratings.rate'},
            'country_name': { '$addToSet': '$country'},
            'break_type_name': { '$addToSet': '$break_type'},
            'old_id': { '$addToSet': '$_id'},
            'img_url': { '$addToSet': '$img_url'}
            } }
    ])
    locations_random = locations_db.aggregate([
        { '$unwind': '$ratings' },
        { '$group': {
            '_id': '$name',
            'average_rating': { '$avg': '$ratings.rate'},
            'country_name': { '$addToSet': '$country'},
            'break_type_name': { '$addToSet': '$break_type'},
            'old_id': { '$addToSet': '$_id'},
            'img_url': { '$addToSet': '$img_url'}
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

    if locations_db.find({ 'ratings.user_name': user }):
        user_in_rating = user

    now = datetime.now().strftime('%Y-%m-%d at %H:%M:%S')
    location = locations_db.find_one({'_id': ObjectId(location_id)})
    
    if 'username' not in session:
        flash('Please log in or register to rate and comment!')
        return redirect(url_for('user'))

    if request.method == 'POST':
        if 'rating' in request.form:
            locations_db.update(
                { '_id': ObjectId(location_id), 'ratings.user_name': user },
                { '$set': { 'ratings.$.rate': request.form.get('rating', type=int) } },
                False, True
            )
            locations_db.update(
                { '_id': ObjectId(location_id), 'ratings.user_name': { '$ne': user } },
                { '$addToSet': { 
                    'ratings': { 
                        'user_name': user, 'rate': request.form.get('rating', type=int) } } },
                False, True
            )
            flash('Thank you for your rating!', 'spot')
            return redirect(url_for('spot', location_id=location_id))
        else:
            locations_db.update(
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
    # Tools for using Python’s json module with BSON
    location_name = dumps(locations_db.find( {}, { '_id': 0, 'name': 1 } ))

    user = user_in_session()
    countries = categories_db.find( { 'country': {'$ne': 'null'} } )
    break_types = categories_db.find( { 'break_type': {'$ne': 'null'} } )
    wave_directions = categories_db.find( { 'wave_direction': {'$ne': 'null'} } )
    bottom = categories_db.find( { 'bottom': {'$ne': 'null'} } )
    facilities = categories_db.find( { 'facilities': {'$ne': 'null'} } )
    hazards = categories_db.find( { 'hazards': {'$ne': 'null'} } )

    return render_template('search.html', user=user, countries=countries, break_types=break_types, wave_directions=wave_directions, bottom=bottom, facilities=facilities, hazards=hazards, location_name=location_name)


@app.route('/search_by_name', methods=['POST'])
def search_by_name():
    user = user_in_session()
    countries = categories_db.find( { 'country': {'$ne': 'null'} } )
    break_types = categories_db.find( { 'break_type': {'$ne': 'null'} } )
    wave_directions = categories_db.find( { 'wave_direction': {'$ne': 'null'} } )
    bottom = categories_db.find( { 'bottom': {'$ne': 'null'} } )
    facilities = categories_db.find( { 'facilities': {'$ne': 'null'} } )
    hazards = categories_db.find( { 'hazards': {'$ne': 'null'} } )

    search_result = locations_db.find_one({'name': { '$regex': request.form['search_by_name'], '$options': 'i' }})

    if search_result == None:
        flash('Your search did not match any of our records. Please refine your search or if you believe we are missing this location, please add it to our collection!', 'search')
        return redirect(url_for('oups'))
    name_search = locations_db.aggregate([
        { '$match': {'name' : { '$regex': search_result['name'], '$options': 'i' } } },
        { '$unwind': '$ratings' },
        { '$group': {
                '_id': '$name',
                'average_rating': { '$avg': '$ratings.rate'},
                'country_name': { '$addToSet': '$country'},
                'break_type_name': { '$addToSet': '$break_type'},
                'old_id': { '$addToSet': '$_id'},
                'img_url': { '$addToSet': '$img_url'}
            } },
        { '$sort': { '_id': 1 } }
    ])

    name_search = list(name_search)

    return render_template('search.html', user=user, countries=countries, break_types=break_types, wave_directions=wave_directions, bottom=bottom, facilities=facilities, hazards=hazards, name_search=name_search)

@app.route('/advanced_search', methods=['POST'])
def advanced_search():
    user = user_in_session()
    countries = categories_db.find( { 'country': {'$ne': 'null'} } )
    break_types = categories_db.find( { 'break_type': {'$ne': 'null'} } )
    wave_directions = categories_db.find( { 'wave_direction': {'$ne': 'null'} } )
    bottom = categories_db.find( { 'bottom': {'$ne': 'null'} } )
    facilities = categories_db.find( { 'facilities': {'$ne': 'null'} } )
    hazards = categories_db.find( { 'hazards': {'$ne': 'null'} } )

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

    adv_search = locations_db.aggregate([
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
            'old_id': { '$addToSet': '$_id'},
            'img_url': { '$addToSet': '$img_url'}
            } },
        { '$sort': { 'average_rating': -1, '_id': 1 } }
    ])

    adv_search = list(adv_search)

    if adv_search == []:
        flash('Your search did not match any of our records. Please refine your search or if you believe we are missing this location, please add it to our collection!', 'search')
        return redirect(url_for('oups'))
    
    return render_template('search.html', user=user, countries=countries, break_types=break_types, wave_directions=wave_directions, bottom=bottom, facilities=facilities, hazards=hazards, adv_search=adv_search)

@app.route('/oups')
def oups():
    return render_template('oups.html')


"""
ADD LOCATION
"""

@app.route('/add_spot', methods=['GET','POST'])
def add_spot():
    # Tools for using Python’s json module with BSON
    location_name = dumps(locations_db.find( {}, { '_id': 0, 'name': 1 } ))
    
    user = user_in_session()
    if user is None:
        flash('Please log in or register to add a new location.', 'add')
        return redirect(url_for('oups'))

    countries = categories_db.find( { 'country': {'$ne': 'null'} } )
    break_types = categories_db.find( { 'break_type': {'$ne': 'null'} } )
    wave_directions = categories_db.find( { 'wave_direction': {'$ne': 'null'} } )
    wind_directions = categories_db.find( { 'wind_direction': {'$ne': 'null'} } )
    swell_directions = categories_db.find( { 'swell_direction': {'$ne': 'null'} } )
    surroundings = categories_db.find( { 'surroundings': {'$ne': 'null'} } )
    bottom = categories_db.find( { 'bottom': {'$ne': 'null'} } )
    facilities = categories_db.find( { 'facilities': {'$ne': 'null'} } )
    hazards = categories_db.find( { 'hazards': {'$ne': 'null'} } )    

    if request.method == 'POST':
        input_location = request.form.to_dict()
        del input_location['action']
        
        add_new = locations_db.insert_one( { 
            'name': request.form['name_input'].lower(),
            'country': request.form['country_input'].lower(),
            'region': request.form['region_input'].lower(),
            'break_type': request.form['break_type_input'],
            'wave_direction': request.form['wave_direction_input'],
            'wind_direction': request.form['wind_direction_input'],
            'swell_direction': request.form['swell_direction_input'],
            'bottom': request.form['bottom_input'],
            'facilities': facilities_to_new(input_location),
            'surroundings': request.form['surroundings_input'],
            'hazards': hazards_to_new(input_location),
            'ratings': [{
                'user_name': session['username'],
                'rate': int(request.form['add_rating']) }],
            'description': request.form['add_description'],
        } )
        get_loc_id = locations_db.find_one({'name': { '$regex': request.form['name_input'], '$options': 'i' }})
        location_id = get_loc_id['_id']
        return redirect(url_for('spot', location_id=location_id))

    return render_template('addSpot.html', user=user, location_name=location_name, countries=countries, break_types=break_types, wave_directions=wave_directions, wind_directions=wind_directions, swell_directions=swell_directions, surroundings=surroundings, bottom=bottom, facilities=facilities, hazards=hazards)

"""
EDIT LOCATION
"""

@app.route('/editSpot/<location_id>', methods=['GET','POST'])
def editSpot(location_id):
    user = user_in_session()
    if user is None:
        flash('Please log in or register to edit any location.', 'add')
        return redirect(url_for('oups'))

    countries = categories_db.find( { 'country': {'$ne': 'null'} } )
    break_types = categories_db.find( { 'break_type': {'$ne': 'null'} } )
    wave_directions = categories_db.find( { 'wave_direction': {'$ne': 'null'} } )
    wind_directions = categories_db.find( { 'wind_direction': {'$ne': 'null'} } )
    swell_directions = categories_db.find( { 'swell_direction': {'$ne': 'null'} } )
    surroundings = categories_db.find( { 'surroundings': {'$ne': 'null'} } )
    bottom = categories_db.find( { 'bottom': {'$ne': 'null'} } )
    facilities = categories_db.find( { 'facilities': {'$ne': 'null'} } )
    hazards = categories_db.find( { 'hazards': {'$ne': 'null'} } )

    location = locations_db.find_one({'_id': ObjectId(location_id)})

    if request.method == 'POST':
        input_location = request.form.to_dict()
        del input_location['action']

        add_new = locations_db.update_one( 
            { '_id': ObjectId(location_id) },
            { '$set': {
                'break_type': request.form['break_type_input'],
                'wave_direction': request.form['wave_direction_input'],
                'wind_direction': request.form['wind_direction_input'],
                'swell_direction': request.form['swell_direction_input'],
                'bottom': request.form['bottom_input'],
                'facilities': facilities_to_new(input_location),
                'surroundings': request.form['surroundings_input'],
                'hazards': hazards_to_new(input_location),
                'description': request.form['add_description']
            } } )
        flash('Thank you for your input!', 'spot')
        return redirect(url_for('spot', location_id=location_id))
            
    return render_template('editSpot.html', user=user, location=location, countries=countries, break_types=break_types, wave_directions=wave_directions, wind_directions=wind_directions, swell_directions=swell_directions, surroundings=surroundings, bottom=bottom, facilities=facilities, hazards=hazards)

"""
ABOUT
"""

@app.route('/about')
def about():
    user = user_in_session()
    return render_template('about.html', user=user, locations=locations_db.find())

"""
LOG IN | LOG OUT and USER PAGE
"""

@app.route('/login', methods=['POST'])
def login():
    error = None
    users = mongo.db.users
    login_user = users.find_one({'name': { '$regex': request.form['username'], '$options': 'i' }})

    if login_user:
        session['username'] = request.form['username'].lower()
        flash('Welcome back!')
        return redirect(url_for('aloha', username=session['username']))
    error = 'Looks like invalid username. Please try to type again or register below'
    return render_template('user.html', error=error)


@app.route('/user')
def user():
    user = user_in_session()
    return render_template('user.html', user=user)


@app.route('/aloha/<username>')
def aloha(username):
    user = username
            
    locations_user = locations_db.find({
        '$or': [
            { 'ratings.user_name': user },
            { 'comments.user_name': user }
            ]
        })

    return render_template('aloha.html', user=user, locations_user=locations_user)


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
        existing_user = users.find_one({'name': { '$regex': request.form['username'], '$options': 'i' }})
        if existing_user is None:
            users.insert({'name' : request.form['username'] })
            session['username'] = request.form['username']
            flash('You were successfully registered!')
            return redirect(url_for('aloha', username=session['username']))
        error = 'That username already exists. Please choose another one.'
    return render_template('register.html', error=error)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT', '5000')),
    debug=True)