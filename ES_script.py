import requests, time, configparser

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

print(r.text)

'''
headers = {'content-type': 'application/json'};
r = requests.post(DT_API_URL + '/api/v1/synthetic/ext/tests?Api-Token=' + DT_API_TOKEN, json=payload, headers=headers);
# Output API response 
print(r);
print(r.text);
'''