import string, re

def verify(isbn):
    stripped = isbn.replace('-', '')
    if not re.match("^\d{9}[\dX]$", stripped):
        return False

    digits = [10 if x == 'X' else int(x) for x in stripped]

    return sum([digits[x]*(10-x) for x in xrange(0, 10)]) % 11 == 0
