from math import *


# Function to generate all prime
# numbers less than n
def SieveOfEratosthenes(n, isPrime):
    # Initialize all entries of boolean
    # array as true. A value in isPrime[i]
    # will finally be false if i is Not a
    # prime, else true bool isPrime[n+1];
    isPrime[0], isPrime[1] = False, False

    for i in range(2, n + 1):
        isPrime[i] = True

    for p in range(2, int(sqrt(n)) + 1):

        # If isPrime[p] is not changed,
        # then it is a prime
        if isPrime[p] == True:

            for i in range(p * 2, n + 1, p):
                isPrime[i] = False


# Function to print a prime pair
# with given product
def findPrimePair(n):
    flag = 0

    # Generating primes using Sieve
    isPrime = [False] * (n + 1)
    SieveOfEratosthenes(n, isPrime)

    # Traversing all numbers to
    # find first pair
    for i in range(2, n):
        x = int(n / i)

        if isPrime[i] & isPrime[x] and x != i and x * i == n:
            return [i, x]
            flag = 1
            break

    if not flag:
        print("No such pair found")

def solution(n):
    count = []
    te = [2,3,5,7,11]
    for t in te:
        while n % t == 0:
            count.append(t)
            n //= t
            if len(count) == 2:
                if n != 1:
                    return [-1, -1]
                else:
                    if count[0] == count[1]:
                        return [-1, -1]
                    else:
                        return count
    until = 30000000
    nums = [False, False] + [True] * (until - 1)
    primes = []
    for i in range(2, until+1):
        if nums[i]:
            primes.append(i)
            for j in range(2*i, until+1, i):
                nums[j] = False
    count = []
    for prime in primes:
        while n % prime == 0:
            count.append(prime)
            n //= prime
            if len(count) == 2:
                if n != 1:
                    return [-1, -1]
                else:
                    if count[0] == count[1]:
                        return [-1, -1]
                    else:
                        return count
    return [-1, -1]

if __name__ == "__main__":
    print(solution(6))
