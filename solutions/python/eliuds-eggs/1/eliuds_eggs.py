def egg_count(display_value):
    div = display_value
    bin = []
    while div != 0:
        r = div % 2
        div = div // 2
        bin.append(r)
    number_of_egg = sum(bin)
    return number_of_egg