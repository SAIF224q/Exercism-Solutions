color_band_list = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]

def label(colors):
    resistance = ""
    if colors[0] != "black":
        resistance += str(color_band_list.index(colors[0]))
    resistance += str(color_band_list.index(colors[1]))
    resistance = int(resistance) * 10**color_band_list.index(colors[2])
    
    if resistance >= 1_000_000_000:
        return f"{resistance // 1_000_000_000} gigaohms"
    elif resistance >= 1_000_000:
        return f"{resistance // 1_000_000} megaohms"
    elif resistance >= 1_000:
        return f"{resistance // 1_000} kiloohms"
    else:
        return f"{resistance} ohms"
    
    pass
