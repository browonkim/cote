def solution(s: str):
    numbers = map(int, s.split())
    return str(min(numbers)) + str(max(numbers))


def solution2(s):
    until = len(s) // 2
    size = len(s)

    def zipper(n):
        temp = s[0:n]
        count = 0
        tempcount = 0
        for i in range(n, size - size%n, n):
            if s[i:i+n] == temp:
                tempcount += 1
            else:
                count += n + (len(str(tempcount)) if tempcount > 1 else 0)
                tempcount = 1
                temp = s[i:i+n]
        if tempcount == 1:
            count = count + len(temp) + size % n
            return count
        else:
            count = count + n + len(str(tempcount)) + size % n
            return count

    minimum = 9999999999999
    for i in range(1, until+1):
        minimum = min(minimum, zipper(i))

    return minimum

if __name__ == '__main__':
    print(solution2("aabbaccc"))