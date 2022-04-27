def classify(number):
    
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    o = 0
    for i in range(1,number):
        if number % i == 0:
            o += i
    if o == number:
        return 'perfect'
    if o > number:
        return 'abundant'
    return 'deficient'
        