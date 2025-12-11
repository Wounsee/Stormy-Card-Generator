import json
def expData(path, data, fmt):
    if not path or not data: return
    try:
        if fmt == "json":
            with open(path, 'w') as f:
                json.dump(data, f, indent=2)
        else:
            with open(path, 'w') as f:
                for x in data:
                    f.write(f"{x['n']}|{x['e']}|{x['c']}\n")
    except: pass