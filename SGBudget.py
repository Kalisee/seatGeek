import sys
import json
import requests
#from time import sleep
#Sometimes using time.sleep library can help bypass API limits if there are strict time constraints

#Hits SeatGeek 'events' API endpoint and filters for ticket prices based on user input
arg = sys.argv[1]
url = "https://api.seatgeek.com/2/events?highest_price.lte=" + arg + "&client_id=<YOUR API CLIENT ID>"

payload={}
headers = {}

#API output formatting
response = requests.request("GET", url, headers=headers, data=payload)
json_object = json.loads(response.text)


#Accepts filtered output from 'highest price' API query and parses the event IDs
#Passes IDs to the 'events' API to query and parse the ID's associated performers and venue stats 
for data in json_object['events']:
	url = "https://api.seatgeek.com/2/events/" + str(data['id']) + "?client_id=<YOUR API CLIENT ID>"
	payload={}
	headers = {}
	response = requests.request("GET", url, headers=headers, data=payload)
	json_object2 = json.loads(response.text)	


	outputPerformer = json_object2['performers'][0]['name']
	outputStats = json_object2['stats']

	#json beautifying
	print(json.dumps(outputPerformer, sort_keys=True, indent=4))
	print(json.dumps(outputStats, sort_keys=True, indent=4))


