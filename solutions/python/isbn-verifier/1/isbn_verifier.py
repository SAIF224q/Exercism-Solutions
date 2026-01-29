def is_valid(isbn):
    n = 10
    a = 0
    digi = 0
    alph = 0
    ex_alph = 0
    for i in isbn:
        if i.isdigit():
            a += int(i)*n
            n = n - 1
            digi += 1
        elif i == "X" and isbn.index(i)== len(isbn)-1:
            a += 10*n
            n = n - 1
            alph += 1
        elif i.isalpha():
            ex_alph += 1
        
    if a % 11 == 0:
        if digi == 9 and alph == 1:
            return True
        elif digi == 10 and alph == 0 and ex_alph == 0:
            return True
    
    return False

