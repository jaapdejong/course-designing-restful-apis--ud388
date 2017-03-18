from geocode import getGeocodeLocation
import json
import httplib2

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

def getFoursquareCredentials():
	with open('foursquare-ud338') as f:
		client_id = f.readline().strip()
		client_secret = f.readline().strip()
		return (client_id, client_secret)

def findARestaurant(mealType, location):
	client_id, client_secret = getFoursquareCredentials()
	
	#1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.
	latitude, longitude = getGeocodeLocation(location);

	#2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
	#HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi
	url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20170318&ll=%s,%s&browse=%s' % (client_id, client_secret, latitude, longitude, mealType))
	h = httplib2.Http()
	result = json.loads(h.request(url,'GET')[1])

	#3. Grab the first restaurant
	firstRestaurant = result['response']['venues'][0]
	name = firstRestaurant['name']
	address = firstRestaurant['location']['formattedAddress']
	#4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
	#5. Grab the first image
	#6. If no image is available, insert default a image url
	icon = firstRestaurant['categories'][0]['icon']
	image = icon['prefix'] + "300x300" + icon['suffix']
	#7. Return a dictionary containing the restaurant name, address, and image url
	return {'name': name, 'address': address, 'image': image}
	
if __name__ == '__main__':
	print findARestaurant("Pizza", "Tokyo, Japan")
	print findARestaurant("Tacos", "Jakarta, Indonesia")
	print findARestaurant("Tapas", "Maputo, Mozambique")
	print findARestaurant("Falafel", "Cairo, Egypt")
	print findARestaurant("Spaghetti", "New Delhi, India")
	print findARestaurant("Cappuccino", "Geneva, Switzerland")
	print findARestaurant("Sushi", "Los Angeles, California")
	print findARestaurant("Steak", "La Paz, Bolivia")
	print findARestaurant("Gyros", "Sydney Australia")

