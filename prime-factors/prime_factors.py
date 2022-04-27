def factors(value):
    if value == 1:
        return []
    f = []
    d = 2
    while value >= d:
        if (value % d == 0):
            value /= d
            f.append(d)
        else:
            d += 1
    
    return f
