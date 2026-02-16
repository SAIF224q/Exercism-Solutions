def transform(legacy_data):
    data = {}
    for key, value in legacy_data.items():
        for value_inside in value:
            data[value_inside.lower()] = key
    
    return dict(sorted(data.items(), key=lambda item: item[1]))
    
