def append(list1, list2):
    return list1 + list2


def concat(lists):
    concat_list = [item for sublist in lists for item in sublist]
    return concat_list

def filter(function, list):
    filter_list = [item for item in list if function(item)]
    return filter_list

def length(list):
    n = 0
    for i in list:
        n += 1
    return n


def map(function, list):
    map_list = [function(item) for item in list]
    return map_list


def foldl(function, list, initial):
    accumulator = initial
    for item in list:
        accumulator = function(accumulator,item)
    return accumulator
    


def foldr(function, list, initial):
    accumulator = initial
    for item in list[::-1]:
        accumulator = function(accumulator,item)
    return accumulator



def reverse(list):
    reverse_list = [item for item in list[::-1]]
    return reverse_list

