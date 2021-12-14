from itertools import permutations

def solution(numbers):
    def is_prime(target):
        if target == 0 or target == 1:
            return False
        if target == 2:
            return True
        for i in range(2, int(target ** 0.5)):
            if target % i == 0:
                return False
        return True

    a = set([int("".join(i)) for j in range(1, len(numbers)+1) for i in permutations(numbers, j)])
    print(a)
    count = 0
    for n in a:
        if is_prime(n):
            count += 1
    return count


if __name__ == "__main__":
    print(solution("17"))
