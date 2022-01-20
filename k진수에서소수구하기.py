def solution(n, k):
    def is_prime(a):
        if a < 2:
            return False
        for i in range(2, a // 2 + 1):
            if a % i == 0:
                return False
        return True

    number = ''
    if k == 10:
        number = str(n)
    else:
        while n > 0:
            number = str(n % k) + number
            n //= k
    count = 0
    stack = ''
    for num in number:
        if num != '0':
            stack += num
        else:
            if len(stack) != 0:
                if is_prime(int(stack)):
                    count += 1
            stack = ''
    if len(stack) != 0:
        if is_prime(int(stack)):
            count += 1
    return count

if __name__ == "__main__":
    print(solution(110011,	10))
