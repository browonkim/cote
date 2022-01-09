from functools import reduce


def clean_names(names):
    return reduce(lambda a, x: a + x + ',', map(lambda s: s[0:1].upper() + s[1:], filter(lambda x: len(x) > 1, names)),
                  "")[:-1]


def outer():
    a = []

    def inner(k: int = 1):
        a.append(k)
        print(a)

    return inner
def check_prime(number):
    for i in range(2, int(number // 2)):
        if number % i == 0:
            return False
    else:
        return True

def find(n: int):
    def find_prime_numbers(k):
        is_prime = [False, False] + [True] * k
        result = []
        for i in range(2, k):
            if is_prime[i]:
                result.append(i)
                for j in range(i*i, k, i):
                    is_prime[i] = False
        return result
    primes = find_prime_numbers(int(n ** 0.5) + 1)
    for prime in primes:
        if n % prime == 0:
            if check_prime(n/prime):
                return [n, n/prime]
            else:
                return [-1, -1]
    return [-1, -1]


if __name__ == "__main__":
    print(find())