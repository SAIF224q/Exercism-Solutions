def reverse(text):
    reversed_string = ""
    for t in range(len(text)-1,-1,-1):
        reversed_string += text[t]
    return reversed_string
