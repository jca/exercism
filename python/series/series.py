def slices(series, length):
  if length > len(series) or length <= 0:
    raise ValueError('Length must be lower then length of series')

  digits = [int(i) for i in series]
  return [digits[i:i+length] for i in xrange(1+len(series)-length)]
