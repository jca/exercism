def tokenize(word):
    letters = list(word)
    letters[0] = letters[0].lower()
    return sorted(letters)

def detect_anagrams(word, candidates):
    mask = tokenize(word)
    return [candidate for candidate in candidates if tokenize(candidate) == mask]
