import httplib2
import json

def getGoogleApiKey():
	with open('google-ud338') as f:
		return f.readline().strip()
		
def getGeocodeLocation(inputString):
	# Use Google Maps to convert a location into Latitute/Longitute coordinates
	# FORMAT: https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=API_KEY
	google_api_key = getGoogleApiKey()
	locationString = inputString.replace(" ", "+")
	url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (locationString, google_api_key))
	h = httplib2.Http()
	result = json.loads(h.request(url,'GET')[1])
	latitude = result['results'][0]['geometry']['location']['lat']
	longitude = result['results'][0]['geometry']['location']['lng']
	return (latitude,longitude)
	

