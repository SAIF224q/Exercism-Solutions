def is_pangram(sentence):
    Pangram = "abcdefghijklmnopqrstuvwxyz"
    for i in Pangram:
        if i not in sentence.lower():
            return False
    return True
