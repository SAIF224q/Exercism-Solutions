def factors(value):
    prime_f = []
    n = 2
    while value != 1:
        if value % n == 0:
            while value % n == 0:
                value = value / n
                prime_f.append(n)
            n += 1
        else:
            n += 1
    return prime_f
        
