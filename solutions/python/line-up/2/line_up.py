def line_up(name, number):
    number_str = str(number)
    last_digi = number_str[-2:] if len(number_str) > 1 else number_str[-1]
    if last_digi not in ["11","12","13"]:
        if number_str[-1] == "1":
            number_str += "st"
        elif number_str[-1] == "2":
            number_str += "nd"
        elif number_str[-1] == "3":
            number_str += "rd"
        else:
            number_str = number_str + "th"
    else:
        number_str += "th"

    message = f"{name}, you are the {number_str} customer we serve today. Thank you!"
    
    return message
    
