def triangle(sides):
    # To confirm if Triangle or Not
    a,b,c = sides
    if a + b >= c and b + c >= a and a + c >= b and a > 0 and b > 0  and c > 0:
        return True
    else:
        return False
    

def equilateral(sides):
    a,b,c = sides
    if triangle(sides):
        if a == b and b == c:
            return True
        else:
            return False
    else:
        return False



def isosceles(sides):
    a,b,c = sides
    if triangle(sides):
        if a==b or b==c or a==c:
            return True
        else:
            return False
    else:
        return False
    



def scalene(sides):
    a,b,c = sides

    if triangle(sides):
        if a!=b and a!=c and b!=c:
            return True
        else:
            return False
    else:
        return False

