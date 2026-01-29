def is_valid(isbn):
    fltr_isbn = isbn.replace("-","")
    if len(fltr_isbn) != 10 :
        return False
    c = 10
    total = 0
    for i in range(10):
        char = fltr_isbn[i]
        if i == 9 and char.upper() == "X":
            value = 10
        elif char.isdigit():
            value = int(char)
        else:
            return False
        total += value*c
        c -= 1
    return total%11 == 0
        
     
        
        
        