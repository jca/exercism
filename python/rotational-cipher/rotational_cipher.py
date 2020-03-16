import string

def rotate(text, key):
    rotate = lambda letters: letters[key:]+letters[0:key]
    trans = string.maketrans(
        string.ascii_letters,
        rotate(string.ascii_lowercase)+rotate(string.ascii_uppercase))

    return text.translate(trans)
