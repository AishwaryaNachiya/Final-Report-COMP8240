reviews = []
filename = "path_to_reviews.json"
with open(filename, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if idx >= 50000:
            break
        obj = json.loads(line)
        reviews.append(obj)