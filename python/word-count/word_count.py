import re
from collections import Counter

def word_count(phrase):
    matches = re.findall(r'[a-z0-9]+(?:\'[a-z0-9]+)?' , phrase.lower())
    return dict(Counter(matches))
