import json

businesses = []
filename = "yelp_academic_dataset_business.json"
with open(filename, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if idx >= 25000:
            break
        obj = json.loads(line)
        businesses.append(obj)