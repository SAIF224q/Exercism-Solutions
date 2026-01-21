def steps(number):
    if number <=0:
        raise ValueError("Only positive integers are allowed")
    n = number
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = n * 3 + 1
        count += 1
    return count
