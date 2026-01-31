def rotate(text, key):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            # Shift lowercase letters
            shifted = ord('a') + (ord(char) - ord('a') + key) % 26
            result.append(chr(shifted))
        elif 'A' <= char <= 'Z':
            # Shift uppercase letters
            shifted = ord('A') + (ord(char) - ord('A') + key) % 26
            result.append(chr(shifted))
        else:
            # Leave non-alphabetic characters unchanged
            result.append(char)
    return ''.join(result)

    



