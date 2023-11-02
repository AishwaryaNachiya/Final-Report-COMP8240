users = []
filename = "path_to_user.json"
with open(filename, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if idx >= 50000:
            break
        obj = json.loads(line)
        users.append(obj)
