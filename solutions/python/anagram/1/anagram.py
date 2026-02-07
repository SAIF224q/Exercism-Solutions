def find_anagrams(word, candidates):
    # Normalize target word: convert to lowercase for comparison
    word_normalized = word.lower()
    # Create a signature for the target word (sorted lowercase letters)
    word_sorted = sorted(word_normalized)
    
    anagrams = []
    
    for candidate in candidates:
        # Skip if candidate is identical to target (not its own anagram)
        if candidate.lower() == word_normalized:
            continue
            
        # Normalize candidate for comparison
        candidate_normalized = candidate.lower()
        
        # Check if sorted letters match (and word is not empty)
        if candidate_normalized and sorted(candidate_normalized) == word_sorted:
            anagrams.append(candidate)
    
    return anagrams
    pass
