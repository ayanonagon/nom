import urllib2

ORDERIN_API_KEY = 'X2RlbGl2ZXJpbmciOjAsIg'
TEST_URL = 'https://r-test.ordr.in/'

def get_restaurants(street, city, zipcode):
    url = (TEST_URL + 'dl/ASAP/' + zipcode + '/' + city + '/' + street).replace(' ', '+')
    return urllib2.urlopen(url).read()

if __name__ == '__main__':
    print get_restaurants('3913 Baltimore Avenue', 'Philadelphia', '19104')
