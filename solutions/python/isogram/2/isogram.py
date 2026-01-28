def is_isogram(string):

    for i in string.lower():
        if i.isalpha() and (string.lower()).count(i) > 1:
            return False
    return True
