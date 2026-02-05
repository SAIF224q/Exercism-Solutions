def resistor_label(colors):
    color_values = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }

    tolerance_values = {
        "grey": 0.05,
        "violet": 0.1,
        "blue": 0.25,
        "green": 0.5,
        "brown": 1,
        "red": 2,
        "gold": 5,
        "silver": 10,
    }

    if len(colors) == 1:
        return "0 ohms"

    if len(colors) == 4:
        value1, value2, multiplier, tolerance_color = colors
        resistance = (color_values[value1] * 10 + color_values[value2]) * (10 ** color_values[multiplier])
        tolerance = tolerance_values[tolerance_color]

    elif len(colors) == 5:
        value1, value2, value3, multiplier, tolerance_color = colors
        resistance = (color_values[value1] * 100 + color_values[value2] * 10 + color_values[value3]) * (10 ** color_values[multiplier])
        tolerance = tolerance_values[tolerance_color]

    else:
        raise ValueError("Invalid number of bands")

    if resistance < 1000:
        unit = "ohms"
    elif 1000 <= resistance < 1000000:
        resistance /= 1000
        unit = "kiloohms"
    else:
        resistance /= 1000000
        unit = "megaohms"
        
    if isinstance(resistance, int):
        return f"{resistance} {unit} ±{tolerance}%"
        
    if resistance.is_integer():
        return f"{int(resistance)} {unit} ±{tolerance}%"
    else:
        return f"{resistance} {unit} ±{tolerance}%"
    
