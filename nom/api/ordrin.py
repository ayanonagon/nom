import urllib2
import simplejson
from food import Restaurant

ORDERIN_API_KEY = 'X2RlbGl2ZXJpbmciOjAsIg'
TEST_URL_R = 'https://r-test.ordr.in/'
TEST_URL_O = 'https://o-test.ordr.in/'

def __find_restaurants(street, city, zipcode):
    """Return a list of JSON objects representing restaurants around a given
    street, city, and zipcode."""
    url = (TEST_URL_R + 'dl/ASAP/' + zipcode + '/' + city + '/' + street).replace(' ', '+')
    return simplejson.loads(urllib2.urlopen(url).read())

def get_menu_items(restaurant_id):
    """Return a list of JSON objects representing menu items for a restaurant
    identified by the give id."""
    url = TEST_URL_R + 'rd/' + str(restaurant_id)
    response = urllib2.urlopen(url).read()
    return simplejson.loads(response)['menu']

def turn_into_restaurant(res):
    return Restaurant(res['city'], res['ad'], res['mino'], res['na'], res['del'], 
            res['is_delivering'], res['id'], res['cu'])


def get_restaurants(street, city, zipcode):
    restaurants = find_restaurants('401 Harvey Road', 'College Station', '77840')
    return [turn_into_restaurant(restaurant) for restaurant in restaurants]

if __name__ == '__main__':
    restaurants = __find_restaurants('401 Harvey Road', 'College Station', '77840')
    for restaurant in restaurants:
        #rest = turn_into_restaurant(restaurant)
        pass
    
    items = get_menu_items(100)
    for item in items:
        print item
