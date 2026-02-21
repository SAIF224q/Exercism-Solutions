def square_root(number):
    #Newton's Method
    x = number  # initial guess
    while True:
        root = (x + number // x) // 2  # integer division
        if root >= x:
            return x
        x = root