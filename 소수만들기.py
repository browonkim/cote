from itertools import combinations


def solution(nums):
    def is_prime(a):
        for i in range(1, a ** (1 / 2)):
            if a % i == 0:
                return False
        else:
            return True

    result = 0
    for n1, n2, n3 in combinations(nums):
        if is_prime(n1 + n2 + n3):
            result += 1

    return result