color_code_dic = {"black":0, "brown":1, "red":2, "orange":3, "yellow":4, "green":5, "blue":6, "violet": 7, "grey":8, "white":9}

def color_code(color):
    return color_code_dic[color]



def colors():
    band_colors = []
    for color in color_code_dic.keys():
        band_colors.append(color)
    return band_colors
        

