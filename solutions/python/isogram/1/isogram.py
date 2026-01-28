def is_isogram(string):
    letters = "abcdefghijklmnopqrstuvwxyz"
    letters_in_string = "".join(string.lower())
    for i in letters_in_string:
        if i in letters and letters_in_string.count(i)>1:
            return False
    return True
