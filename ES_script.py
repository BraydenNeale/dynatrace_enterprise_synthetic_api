import requests, time, configparser, json

config = configparser.ConfigParser()
config_path = './config.ini'
config.read(config_path)

DT_API_URL = config.get('dynatrace','DT_API_URL')
DT_API_TOKEN = config.get('dynatrace', 'DT_API_TOKEN')
DCRUM_QUERY_URL = config.get('dcrum', 'DCRUM_QUERY_URL')
DCRUM_USER = config.get('dcrum', 'DCRUM_USER')
DCRUM_PWD = config.get('dcrum', 'DCRUM_PWD')

r = requests.get(DCRUM_QUERY_URL, auth=(DCRUM_USER, DCRUM_PWD))

if (not r.status_code == requests.codes.ok):
    exit()

#test_data = r.json()['formattedData']
with open('example_payload.json') as f:
    test_data = json.load(f)['formattedData']

# TODO - group like steps into a single test
# currently just treating all steps as invidual tests
steps = []
for s in test_data:
	step = {}
	step['name'] = s[0]
	step['start_time'] = s[1]
	step['pass'] = True if s[2] == '100.0' else False
	step['response_time'] = s[3]
	steps.append(step)

for step in steps:
	print('\n')
	for k,v in step.items():
		print(v)
		# Add to request

'''
headers = {'content-type': 'application/json'};
r = requests.post(DT_API_URL + '/api/v1/synthetic/ext/tests?Api-Token=' + DT_API_TOKEN, json=payload, headers=headers);
# Output API response 
print(r);
print(r.text);
'''