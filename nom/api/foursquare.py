import datetime
import urllib2
import simplejson

FOURSQUARE_CLIENT_ID = 'YKLQLLARWZ2F31BS1XTA2BTJYGJ2TUPVTRLK3G2DZPH2RWYA'
FOURSQUARE_CLIENT_SECRET = 'A5BOWQGUQQLTZDT3ECDSAP24J0GFFIYYTUQRV4UT51JU0QCH'

def __get_current_date_stamp():
    """Return the current date in the format YYYYMMDD."""
    now = datetime.datetime.now()
    return str(now.year) + str(now.month).zfill(2) + str(now.day).zfill(2)
 
def get_locations_near(lat, lon):
    """Return a list of Foursquare venues near the given latlon."""
    url = 'https://api.foursquare.com/v2/venues/search?ll=%(lat)s,%(lon)s&client_id=%(client_id)s&client_secret=%(client_secret)s&v=%(date)s' % {"lat": lat, "lon": lon, "client_id": FOURSQUARE_CLIENT_ID, "client_secret": FOURSQUARE_CLIENT_SECRET, "date": __get_current_date_stamp()} 
    response = urllib2.urlopen(url).read()
    return simplejson.loads(response)["response"]["venues"]

if __name__ == '__main__':
    print get_locations_near(40.7,-74)
