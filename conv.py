import json

f = open('/tmp/1.json')

data = json.load(f)

for i in data['data']:
    print(i['worker']+';'+i['type']+';'+str(i['total']))

f.close()