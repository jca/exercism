def distance(strand_a, strand_b):
    if (len(strand_a) != len(strand_b)):
        raise ValueError('Invalid lengths!')
    else:
        return sum(map(lambda a,b: a!=b, strand_a, strand_b))
