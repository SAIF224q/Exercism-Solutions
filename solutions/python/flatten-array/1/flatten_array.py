def flatten(iterable):
    flat_list = []
    for element in iterable:
        if isinstance(element, list):
            flat_list.extend(flatten(element))
        elif element is not None:
            flat_list.append(element)
    return flat_list


