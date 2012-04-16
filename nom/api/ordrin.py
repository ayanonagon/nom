import urllib2
import simplejson

ORDERIN_API_KEY = 'X2RlbGl2ZXJpbmciOjAsIg'
TEST_URL = 'https://r-test.ordr.in/'

def get_restaurants(street, city, zipcode):
    url = (TEST_URL + 'dl/ASAP/' + zipcode + '/' + city + '/' + street).replace(' ', '+')
    return simplejson.loads(urllib2.urlopen(url).read())

if __name__ == '__main__':
    restaurants = get_restaurants('401 Harvey Road', 'College Station', '77840')
    for restaurant in restaurants:
        print restaurant
