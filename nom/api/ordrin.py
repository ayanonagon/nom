import urllib2
import simplejson
from food import Restaurant
from food import Item
from food import Category

ORDERIN_API_KEY = 'X2RlbGl2ZXJpbmciOjAsIg'
TEST_URL = 'https://r-test.ordr.in/'

def __find_restaurants(street, city, zipcode):
    """Return a list of JSON objects representing restaurants around a given
    street, city, and zipcode."""
    url = (TEST_URL + 'dl/ASAP/' + zipcode + '/' + city + '/' + street).replace(' ', '+')
    return simplejson.loads(urllib2.urlopen(url).read())

def get_menu_items(restaurant_id):
    """Return a list of JSON objects representing menu items for a restaurant
    identified by the give id."""
    url = TEST_URL + 'rd/' + str(restaurant_id)
    response = urllib2.urlopen(url).read()
    return simplejson.loads(response)

def turn_into_restaurant(res):
    return Restaurant(res['city'], res['ad'], res['mino'], res['na'], res['del'], 
            res['is_delivering'], res['id'], res['cu'])


def get_restaurants(street, city, zipcode):
    restaurants = find_restaurants('401 Harvey Road', 'College Station', '77840')
    rests = []
    for restaurant in restaurants:
        rests.append(turn_into_restaurant(restaurant))
    return rests
    

if __name__ == '__main__':
    restaurants = __find_restaurants('401 Harvey Road', 'College Station', '77840')
    for restaurant in restaurants:
        #print restaurant, "\n", "\n"
        pass
    
    info = get_menu_items(147)
    items = info['menu']
    for item in items:
        print item, "\n", "\n"

    print info['meal_name']

