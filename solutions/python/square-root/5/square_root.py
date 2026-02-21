def square_root(number):
    #Heron's Method
    guess = number
    while True:
        better_guess = (guess + number // guess) // 2
        if better_guess >= guess:
            return guess
        guess = better_guess