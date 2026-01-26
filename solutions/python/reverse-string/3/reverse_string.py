def reverse(text):
    n = []
    for t in text:
        n.insert(0,t)
        
    reversed_string = "".join(n)   
    return reversed_string
