from rapidconnect import RapidConnect
import requests
import json

def coordinates(address):
	rapid = RapidConnect('FinanceBot', 'de800779-fee6-4bc8-ac71-0c239d9264f5');

	result = rapid.call('GoogleGeocodingAPI', 'addressToCoordinates', { 
		'apiKey': 'AIzaSyBQxQDQ5WEpn2hO9W5UaTD0iJe5xvaEsy0',
		'address': address
	});

	return eval(result);

def find_atms(lat, lng, rad):
	req_url = 'http://api.reimaginebanking.com/atms?lat=' + str(lat) + '&lng=' + str(lng) + '&rad=' + str(rad) + '&key=22827101aa2aed5f76342f276b3e38fb'
	r = requests.get(req_url)
	return json.dumps(r.json(), indent=2)

def main():
	debug = 1;
	if debug == 1:
		address = '6930 Old Dominion Dr, McLean, VA 22101'
	else:
		address = raw_input("Enter an address: ")

	coords = coordinates(address)
	atms = find_atms(coords['lat'], coords['lng'], raw_input("Enter the radius: "))