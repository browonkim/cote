def getOptimalString(s):
    count = [0, 0]
    result = ''
    for i in s:
        count[int(i)] += 1
    n = 0
    while count[0] > 0 and count[1] > 0:
        if n % 2 == 0:
            result += '1'
            count[1] -= 1
        else:
            result += '0'
            count[0] -= 1
        n += 1
    if count[0] == 0:
        result += '1' * count[1]
    elif count[1] == 0:
        result += '0' * count[0]
    return ''.join(reversed(result))

if __name__ == '__main__':
    print(getOptimalString('011'))