import sys
import json
import requests
#from time import sleep

arg = sys.argv[1]
arg2 = sys.argv[2]

url = "https://api.seatgeek.com/2/events?datetime_utc.gte=" + arg + "&datetime_utc.lte=" + arg2 + "&client_id=<YOUR CLIENT ID>"


payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

json_object = json.loads(response.text)

for data in json_object['events']:
	url = "https://api.seatgeek.com/2/events/" + str(data['id']) + "?client_id=<YOUR CLIENT ID>"
	payload={}
	headers = {}
	response = requests.request("GET", url, headers=headers, data=payload)
	json_object2 = json.loads(response.text)	

	outputDate = json_object2['datetime_utc']
	outputPerformer = json_object2['performers'][0]['name']
	outputStats = json_object2['stats']

	print(json.dumps(outputDate, sort_keys=True, indent=4))
	print(json.dumps(outputPerformer, sort_keys=True, indent=4))
	print(json.dumps(outputStats, sort_keys=True, indent=4))