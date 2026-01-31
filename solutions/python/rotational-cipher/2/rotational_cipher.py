def rotate(text, key):
    plain = "abcdefghijklmnopqrstuvwxyz"
    rotate_plain = plain[-key:] + plain[:-key]
    cipher = []
    for i in text:
        indx = 0
        if i.isalpha():
            if i.isupper():
                indx = rotate_plain.index(i.lower())
                cipher.append(plain[indx].upper())
            else:
                indx = rotate_plain.index(i)
                cipher.append(plain[indx])
        else:
            cipher.append(i)
    return "".join(cipher)
            

    



