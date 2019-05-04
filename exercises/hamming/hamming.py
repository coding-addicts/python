def distance(strand_a, strand_b):
  if len(strand_a) != len(strand_b):
    raise ValueError('DNA strands differ in length.')

  distance = 0
  for a, b in zip(strand_a, strand_b):
    if a != b:
      distance += 1
  return distance
