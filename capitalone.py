from rapidconnect import RapidConnect
import requests
import json

def coordinates(address):
	rapid = RapidConnect('FinanceBot', 'de800779-fee6-4bc8-ac71-0c239d9264f5');

	result = rapid.call('GoogleGeocodingAPI', 'addressToCoordinates', { 
		'apiKey': 'AIzaSyBQxQDQ5WEpn2hO9W5UaTD0iJe5xvaEsy0',
		'address': address
	});

	return result;

def find_atms(lat, lng, rad):
	url = 'http://api.reimaginebanking.com/atms'
	apiKey = '22827101aa2aed5f76342f276b3e38fb'
	payload = {   
	    "lat": lat,
	    "lng": lng,
	    "accessibility": True,
	    "rad": rad,
	    "key": apiKey
	  }
	print 
	r = requests.get(url, params = payload, headers={'content-type':'application/json'})
	arr = r.json()[u'data']
	# print json.dumps(r.json(), indent=2)
	for dic in arr:
		dic['dist'] = (dic[u'geocode'][u'lat'] - lat)**2 + \
 		 (dic[u'geocode'][u'lng'] - lng)**2
	sort = sorted(arr, key=lambda dic: dic['dist'])
	for i in range(len(arr)):
		print arr[i]['dist']
	return sort


def run_atm(rad, address):
	if rad is '':
		rad = '1'
	else:
		rad = str(int(round(float(rad))))
	if address is '':
		address = '6930 Old Dominion Dr, McLean, VA 22101'

	coords = coordinates(address)
	atms = find_atms(coords['lat'], coords['lng'], rad)
	#for atm in atms:
	#	print atm['dist'], atm[u'_id'], '(', atm[u'geocode'][u'lat'], ', ', atm[u'geocode'][u'lng'], ')'
	
	best_atm = atms[0]
	address = best_atm[u'address']
	location = "%s %s, %s %s %s" % (address[u'street_number'],\
	 address[u'street_name'], address[u'city'],\
	 address[u'state'], address[u'zip'], )

	return (rad, str(location))

### NEED TO CHANGE THIS BELOW CODE TO WORK WITH A LIST, SINCE BRANCHES ARE DISPLAYED IN A LIST NOT A DICTIONARY ###
### NEED TO CHANGE THIS BELOW CODE TO WORK WITH A LIST, SINCE BRANCHES ARE DISPLAYED IN A LIST NOT A DICTIONARY ###
### NEED TO CHANGE THIS BELOW CODE TO WORK WITH A LIST, SINCE BRANCHES ARE DISPLAYED IN A LIST NOT A DICTIONARY ###
### NEED TO CHANGE THIS BELOW CODE TO WORK WITH A LIST, SINCE BRANCHES ARE DISPLAYED IN A LIST NOT A DICTIONARY ###
### NEED TO CHANGE THIS BELOW CODE TO WORK WITH A LIST, SINCE BRANCHES ARE DISPLAYED IN A LIST NOT A DICTIONARY ###
### NEED TO CHANGE THIS BELOW CODE TO WORK WITH A LIST, SINCE BRANCHES ARE DISPLAYED IN A LIST NOT A DICTIONARY ###
### NEED TO CHANGE THIS BELOW CODE TO WORK WITH A LIST, SINCE BRANCHES ARE DISPLAYED IN A LIST NOT A DICTIONARY ###
### NEED TO CHANGE THIS BELOW CODE TO WORK WITH A LIST, SINCE BRANCHES ARE DISPLAYED IN A LIST NOT A DICTIONARY ###


def find_branches(lat, lng, rad):
	url = 'http://api.reimaginebanking.com/branches'
	apiKey = '22827101aa2aed5f76342f276b3e38fb'
	payload = {   
	    "lat": lat,
	    "lng": lng,
	    "accessibility": True,
	    "rad": rad,
	    "key": apiKey
	  }
	r = requests.get(url, params = payload)
	### NEED TO CHANGE THIS COMMENTED OUT CODE TO WORK WITH A LIST, SINCE BRANCHES ARE DISPLAYED IN A LIST NOT A DICTIONARY ###
	# arr = r.json()[u'data']
	# for dic in arr:
	# 	dic['dist'] = (dic[u'geocode'][u'lat'] - lat)**2 + (dic[u'geocode'][u'lng'] - lng)**2
	# sort = sorted(arr, key=lambda dic: dic['dist'])
	return sort


def run_branches(rad, address):
	if rad is '':
		rad = '1'
	else:
		rad = str(int(round(float(rad))))
	if address is '':
		address = '6930 Old Dominion Dr, McLean, VA 22101'

	coords = coordinates(address)
	branches = find_branches(coords['lat'], coords['lng'], rad)

	#for atm in atms:
	#	print atm['dist'], atm[u'_id'], '(', atm[u'geocode'][u'lat'], ', ', atm[u'geocode'][u'lng'], ')'
	
	best_branch = branches[0]
	address = best_branch[u'address']
	location = "%s %s, %s %s %s" % (address[u'street_number'], address[u'street_name'], address[u'city'],\
	 address[u'state'], address[u'zip'], )

	return (rad, str(location))
