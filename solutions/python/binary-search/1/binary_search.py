def find(search_list, value):
    bsl = search_list
    if value not in search_list:
        raise ValueError("value not in array")
    song_no = None
    while song_no != value:
        idx = len(bsl)//2
        song_no = bsl[idx]
        if song_no == value:
            return search_list.index(song_no)
        elif song_no > value:
            bsl = bsl[:idx]
        else:
            bsl = bsl[idx+1:]
