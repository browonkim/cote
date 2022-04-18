from itertools import combinations


def solution(arr, k, t):
    answer = 0
    for i in range(k, len(arr)+1):
        iteration = combinations(arr, i)
        li = [x for x in iteration if sum(x) <= t]
        answer += len(li)
    return answer


if __name__ == "__main__":
    print(solution([2, 5, 3, 8, 1], 3, 11))
