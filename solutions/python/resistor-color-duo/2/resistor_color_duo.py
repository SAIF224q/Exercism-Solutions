color_band_list = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]

def value(colors):
    return int(str(color_band_list.index(colors[0])) + str(color_band_list.index(colors[1])))

