def line_up(name, number):
    last_digi = str(number)[-1]
    number_str = str(number)
    if last_digi == "1" and number_str[-2:] != "11":
        number_str = number_str + "st"
    elif last_digi == "2" and number_str[-2:] != "12":
        number_str = number_str + "nd"
    elif last_digi == "3" and number_str[-2:] != "13":
        number_str = number_str + "rd"
    else:
        number_str = number_str + "th"

    message = f"{name}, you are the {number_str} customer we serve today. Thank you!"
    
    return message
    
