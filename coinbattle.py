def solution(a, b):
    if a == 0 and b == 0:
        return [0, 0]
    if a == b:
        return [0, 1]
    if a == 0 or b == 0:
        return [0, 1]
    if (a == 1 and b == 2) or (a == 2 and b == 1):
        return [1, 2]
    elif abs(a - b) == 1:
        return [0, 3]
    count = 0
    cur = 0
    if a > b:
        b = 3
        a = a - b + 3
    else:
        a = 3
        b = b - a + 3
    
    return [cur, count + 3]
