color_band_list = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]

def value(colors):
    resitance = ""
    r = 0
    for color in colors:
        if r==2:
            break
        resitance += str(color_band_list.index(color))
        r+=1
        
    return int(resitance)

