def translate(text):
    vowels = set('aeiou')
    
    def translate_word(word):
        if word[0] in vowels or word.startswith('xr') or word.startswith('yt'):
            return word + 'ay'
        
        for i in range(len(word) - 1):
            if word[i:i+2] == 'qu':
                if i == 0 or all(c not in vowels for c in word[:i]):
                    return word[i+2:] + word[:i+2] + 'ay'
                break  
        
        for i in range(1, len(word)):  # Start from index 1, not 0
            if word[i] == 'y':
                if all(c not in vowels for c in word[:i]):
                    return word[i:] + word[:i] + 'ay'
                break 
        
        for i in range(len(word)):
            if word[i] in vowels:
                return word[i:] + word[:i] + 'ay'
        
        return word + 'ay'
    
    words = text.split()
    translated_words = [translate_word(word) for word in words]
    
    return ' '.join(translated_words)