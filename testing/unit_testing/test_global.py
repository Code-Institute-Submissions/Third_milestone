from global_functions import *


def facilities_to_Array(advanced_search_results):
    checkbox_results = []
    for key, value in advanced_search_results.items():
        if value == 'include':
            checkbox_results.append(key)
    if checkbox_results == []:
        return {'$exists': 'True'}
    return {'$all': checkbox_results}

advanced_search_results = {'': ''}
# scenario1 - user does not select any of the facilities for advance search
test_are_equal(facilities_to_Array(advanced_search_results), {'$exists': 'True'})
# scenario2 - user selects one facilities for advance search
advanced_search_results = {'lack of facilities': 'include'}
test_are_equal(facilities_to_Array(advanced_search_results), {'$all': ['lack of facilities']})
# scenario3 - user selects two facilities for advance search
advanced_search_results = {'accommodation': 'include', 'showers': 'include'}
test_are_equal(facilities_to_Array(advanced_search_results), {'$all': ['accommodation', 'showers']})
# scenario4 - user selects other categories beside facilities for advance search
advanced_search_results = {'country_selection': 'England', 'break_type_selection': 'beach break', 'wave_direction_selection': 'right', 'bottom_selection': 'sand', 'no life guards': 'exclude'}
test_are_equal(facilities_to_Array(advanced_search_results), {'$exists': 'True'})


print('All the test for "facilities_to_Array" passed')


def hazards_to_new(input_location):
    checkbox_results = []
    for key, value in input_location.items():
        if value == 'hazard':
            checkbox_results.append(key)
    if checkbox_results == []:
        checkbox_results = ['hazards free']
    return checkbox_results

input_location = {'': ''}
# scenario1 - user does not select any of the hazards for new location
test_are_equal(hazards_to_new(input_location), ['hazards free'])
# scenario2 - user selects one hazard type
input_location = {'pollution': 'hazard'}
test_are_equal(hazards_to_new(input_location), ['pollution'])
# scenario3 - user selects three hazards together with other categories
input_location = {'name_input': 'White Sands', 'country_input': 'Ireland', 'region_input': 'Clare', 'break_type_input': 'beach break', 'wave_direction_input': 'right', 'wind_direction_input': 'south-east', 'swell_direction_input': 'south-east', 'bottom_input': 'rocky reef', 'surroundings_input': 'village', 'img_url_input': '', 'pollution': 'hazard', 'urchins': 'hazard', 'rocks': 'hazard', 'add_rating': '3', 'add_description': 'some description'}
test_are_equal(hazards_to_new(input_location), ['pollution', 'urchins', 'rocks'])
# scenario4 - user selects other categories leaving hazards blank
input_location = {'name_input': 'White Sands', 'country_input': 'Ireland', 'region_input': 'Clare', 'break_type_input': 'beach break', 'wave_direction_input': 'right', 'wind_direction_input': 'south-east', 'swell_direction_input': 'south-east', 'bottom_input': 'rocky reef', 'surroundings_input': 'village', 'img_url_input': '', 'add_rating': '3', 'add_description': 'some description'}
test_are_equal(hazards_to_new(input_location), ['hazards free'])

print('All the test for "hazards_to_new" passed')


def sort_locations(sort_by):
    sort_locations = ''
    if sort_by == 'rate':
        sort_locations = {'average_rating': -1, '_id': 1}
        return sort_locations
    elif sort_by == 'country':
        sort_locations = {'country_name': 1, '_id': 1}
        return sort_locations
    elif sort_by == 'name':
        sort_locations = {'_id': 1}
        return sort_locations

# scenario1 - user selects option to sort by location rate
test_are_equal(sort_locations('rate'), {'average_rating': -1, '_id': 1})
# scenario2 - user selects option to sort by location country
test_are_equal(sort_locations('country'), {'country_name': 1, '_id': 1})
# scenario3 - user selects option to sort by location name
test_are_equal(sort_locations('name'), {'_id': 1})
# scenario4 - user does not selects any of the filter options
test_are_equal(sort_locations(''), None)

print('All the test for "sort_locations" passed')
