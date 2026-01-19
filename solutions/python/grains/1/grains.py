def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    numberOfGraines = 0
    n = 1
    for i in range(1,number+1):
        if i == 1:
            numberOfGraines = 1
        else:
            numberOfGraines = numberOfGraines * 2
    return numberOfGraines
            


def total():
    totalGrains = 0
    for i in range(1,65):
        totalGrains += square(i)
    return totalGrains
