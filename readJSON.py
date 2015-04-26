import json
from pprint import pprint

with open('sa_raw.json') as data_file:    
    data = json.load(data_file)

#pprint(data)
c=0
for  i in data["data"]:
	#print str(data["data"]["message"])
	c += 1

print data["data"][0]["message"]
print str(c)
'''
data["maps"][0]["id"]
data["masks"]["id"]
data["om_points"]
'''