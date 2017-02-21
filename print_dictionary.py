import json
with open('definitions.txt', 'r') as json_data:
    d = json.load(json_data)
print(json.dumps(d, indent=0, sort_keys=True))
