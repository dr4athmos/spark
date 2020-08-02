import json, pprint, requests, textwrap, time

host = 'http://90.147.190.27:8998'
data = {'kind': 'pyspark','name':'prog'}
headers = {'Content-Type': 'application/json'}

r = requests.post(host + '/sessions', data=json.dumps(data), headers=headers)

print("### Session created")
#print(r.headers)
#print(r.json())
r.json()

location = r.headers['Location']
session_url = host + location

r = requests.get(session_url, headers=headers)
print("--- Session start command sended")
#print(r.headers)
#print(r.json())
r.json()

state = ""
while state != "ok": 
    print("--- Waiting session start...")
    statements_url = session_url + '/statements'    
    data = {'code': 'import numpy'}
    r = requests.post(statements_url, data=json.dumps(data), headers=headers)
    
    
    #print(r.headers)
    #print(r.json())
    resp = r.json()
    if isinstance(resp,dict):
        state = "ok"
        print("--- First job sended")
    time.sleep(1)

time.sleep(2)

data = {'code': '2 + 2'}
r = requests.post(statements_url, data=json.dumps(data), headers=headers)
print("--- Second job sended")

time.sleep(2)
data = {'code': '3 + 3'}
r = requests.post(statements_url, data=json.dumps(data), headers=headers)
print("--- Third job sended")