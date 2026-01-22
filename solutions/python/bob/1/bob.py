def response(hey_bob):
    
    ask = hey_bob.strip()
    
    if ask == "":
        return "Fine. Be that way!"    
    elif ask.isupper():
        if ask[-1] == "?":
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    elif ask[-1] == "?":
        return "Sure."
    else:
        return "Whatever."
        
