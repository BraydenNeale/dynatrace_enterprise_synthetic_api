"""
Example script that shows how to send external synthetic data into Dynatrace.
"""
import requests, time

YOUR_DT_API_URL = '<DT_API>'
YOUR_DT_API_TOKEN = '<TOKEN>';
DCRUM_QUERY_URL = "<DCRUM_URL>/rest/dmiquery/getDMIData3?appId=CVENT&viewId=TransAct&dimensionIds=['bgTrans','transTimestamp']&metricIds=['Avb','transTime']&resolution=r&dimFilters=[]&metricFilters=[]&sort=[['transTimestamp',DESC]]&topFilter=1000&timePeriod=1H&numberOfPeriods=1&dataSourceId=ALL_AGGR"

syntheticData = requests.get(DCRUM_QUERY_URL);
responseTime = syntheticRequest.elapsed.total_seconds();

success = False;
if (syntheticRequest.status_code == requests.codes.ok): 
    success = True;
	
print ('Synthetic request - Response time:' + str(responseTime) + 's Status code:' + str(syntheticRequest.status_code) + " Success:" + str(success));

timestamp = time.time() * 1000;

payload = {
    "messageTimestamp": timestamp,
    "syntheticEngineName": "My test",
    "syntheticEngineIconUrl": "http://assets.dynatrace.com/global/icons/cpu_processor.png",
    "locations": [{
         "id": "1",
         "name": "Linz"
    }],
    "tests" : [ {
        "id": "1",
        "title": "Example.com",
        "testSetup":  "Python script",
        "drilldownLink": "http://example.com/",
        "enabled": True,
        "locations": [ {
            "id": "1",
            "enabled": True
        }],
        "steps": [ {
            "id": 1,
            "title": "Get request example.com"
        }]
    }],    
    "testResults": [{
        "id": "1",
        "scheduleIntervalInSeconds": 60,
        "totalStepCount": 1,
        "locationResults": [{
            "id": "1",
            "startTimestamp": timestamp,
            "success": success,
            "stepResults": [{
                "id" : 1,
                "startTimestamp": timestamp,
                "responseTimeMillis": responseTime * 1000
            }]
    }]
}]};

headers = {'content-type': 'application/json'};
r = requests.post(YOUR_DT_API_URL + '/api/v1/synthetic/ext/tests?Api-Token=' + YOUR_DT_API_TOKEN, json=payload, headers=headers);
# Output API response 
print(r);
print(r.text);