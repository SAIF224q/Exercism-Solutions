plain = "abcdefghijklmnopqrstuvwxyz"
cipher = "zyxwvutsrqponmlkjihgfedcba"

def encode(plain_text):
    plain_text = plain_text.replace(" ", "").lower()
    encode_output = ""
    count = 0
    for letter in plain_text:
        if count == 5:
            encode_output += " "
            count = 0
        if letter.isalpha():
            encode_output += cipher[plain.index(letter)]
            count += 1
        elif letter.isalnum():
            encode_output += letter
            count += 1
    
    return encode_output.strip()
        


def decode(ciphered_text):
    ciphered_text = ciphered_text.replace(" ", "").lower()
    decode_output = ""
    for letter in ciphered_text:
        if letter.isalpha():
            decode_output += plain[cipher.index(letter)]
        else:
            decode_output += letter
    return decode_output
