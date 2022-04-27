def is_isogram(string):
    count = {}
    string = string.lower()
    
    for char in string:
        if char not in count and char != '-' and char != ' ':
            count[char] = 1
        elif char in count:
            count[char] += 1
    if max(count.values(), default = 1) == 1:
        return True    
    return False