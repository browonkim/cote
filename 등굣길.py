def solution(m, n, puddles):
    answer = 0
    arr = [[1] * n for i in range(m)]
    for i in puddles:
        arr[i[0] - 1][i[1] - 1] = 0
    # 첫번째 행, 열 연산 (초기화)
    for i in range(1, n):
        if arr[0][i - 1] == 0:
            arr[0][i] = 0
    for j in range(1, m):
        if arr[j - 1][0] == 0:
            arr[j][0] = 0
    for i in range(1, m):
        for j in range(1, n):
            if arr[i][j] != 0:
                arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
    return arr[m - 1][n - 1]


if __name__ == "__main__":
    print(solution(4, 3, [[2, 2]]))
