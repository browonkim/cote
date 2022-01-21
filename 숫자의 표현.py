def solution(n):
    answer = 0
    for i in range(1, n // 2 + 2):
        s = 0
        for j in range(i, n // 2 + 3):
            if s >= n:
                if s == n:
                    answer += 1
                break
            s += j
    return answer + 1


if __name__ == "__main__":
    print(solution(15))
