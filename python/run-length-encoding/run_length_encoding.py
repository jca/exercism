from itertools import groupby, imap

def decode(string):
    length = 1;
    decoded = [];
    for is_digit, characters in groupby(string, str.isdigit):
        token = ''.join(characters)
        if is_digit:
            length = int(token)
        else:
            decoded.append(token[0] * length)
            decoded.append(token[1:])
            length = 1
    return ''.join(decoded)

def encode(string):
    return ''.join(x if reps == 1 else str(reps)+x for x, reps in imap(lambda x: (x[0], len(list(x[1]))), groupby(string)))
