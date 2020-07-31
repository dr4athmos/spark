import json, pprint, requests, textwrap
host = 'http://90.147.190.27:8998' # Livy public ip

# Change the range id Ids is in another range
for i in range(0,100):
    r = requests.delete(host + '/sessions/'+ str(i))