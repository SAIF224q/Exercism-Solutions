def square_root(number):
    # We are going to dic where we will put roots for each number(You are only required to handle cases where the result is a positive whole number.)
    roots_for_all = {}
    for i in range(1,number+1):
        roots_for_all[i**2] = i
    return roots_for_all[number]

