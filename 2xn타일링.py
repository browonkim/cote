from functools import reduce
import operator as op


def solution(n):
    def nCr(n, r):
        r = min(r, n - r)
        numerator = reduce(op.mul, range(n, n - r, -1), 1)
        denominator = reduce(op.mul, range(1, r + 1), 1)
        return numerator//denominator

    max_row = n // 2
    result = 0
    for rows in range(max_row + 1):
        result += nCr(n-rows, rows)

    return result


if __name__ == "__main__":
    print(solution(1))
