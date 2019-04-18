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