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

def fetch_menu_items(restaurant_id):
    """Return a list of JSON objects representing menu items for a restaurant
    identified by the give id."""
    url = TEST_URL + 'rd/' + str(restaurant_id)
    response = urllib2.urlopen(url).read()
    return simplejson.loads(response)

def get_menu_items(restaurant_id):
    """Returns the items a restaurant has, as a list of categories"""
    items = fetch_menu_items(restaurant_id)['menu']
    cats = []
    for item in items:
        if 'is_orderable' in item and item['is_orderable'] == 0:
            #item is a category (presumably)
            children = []
            for child in item['children']:
                #Custom enchilada is a child
                subchildren = []
                if 'children' in child:
                    for subchild in child['children']:
                        #Custom enchilada meat is a subchild
                        subsubchildren = []
                        if 'children' in subchild:
                            for subsubchild in subchild['children']:
                                #with chicken is a subsubchild
                               subsubchildren.append(make_item(subsubchild, []))
                        subchildren.append(make_item(subchild, subsubchildren))
                children.append(make_item(child, subchildren))
        cats.append(Category(get_key_if_exists(item, 'name', ''), children)) 
    return cats



def make_item(dic, children):
    price = get_key_if_exists(dic, 'price', '0.00')
    iid = get_key_if_exists(dic, 'id', '0')
    name = get_key_if_exists(dic, 'name', '')
    description = get_key_if_exists(dic, 'description', '')
    return Item(name, price, description, iid, children)



def get_key_if_exists(dic, key, other_val):
    if key in dic:
        return dic[key]
    return other_val




def turn_into_restaurant(res):
    return Restaurant(res['city'], res['ad'], res['mino'], res['na'], res['del'], 
            res['is_delivering'], res['id'], res['cu'])


def get_restaurants(street, city, zipcode):
    restaurants = find_restaurants('401 Harvey Road', 'College Station', '77840')
    return [turn_into_restaurant(restaurant) for restaurant in restaurants]

if __name__ == '__main__':
    restaurants = __find_restaurants('401 Harvey Road', 'College Station', '77840')
    for restaurant in restaurants:
        #print restaurant, "\n", "\n"
        pass
    
    cats = get_menu_items(147)
    for cat in cats:
        print cat.name, "\n"

