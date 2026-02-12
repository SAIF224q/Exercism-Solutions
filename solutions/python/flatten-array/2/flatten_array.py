def flatten(iterable):
    flat_list = []
    for ele in iterable:
        if type(ele) == list:
            flat_list.extend(flatten(ele))
        elif ele is not None:
            flat_list.append(ele)
    return flat_list
    
    

