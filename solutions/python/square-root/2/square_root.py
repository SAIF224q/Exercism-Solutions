def square_root(number):
    #linear method
    i = 1
    while i * i < number:
        i += 1
    return i if i * i == number else None
