def sieve(limit):
    multiples = set()
    primes = []

    for i in xrange(2, limit+1):
      if i not in multiples:
        primes.append(i)
        multiples = multiples.union(set(xrange(i*2, limit+1, i)))

    return primes