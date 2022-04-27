def distance(strand_a, strand_b):
    return sum(i != j for i, j in zip(strand_a, strand_b))
