from functools import reduce


def solution(n, results):
    m = [[0]*n for i in range(n)]
    for winner, loser in results:
        m[winner-1][loser-1] = 1
        m[loser-1][winner-1] = -1
    for i in range(n):
        m[i][i] = 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if m[i][j] == 0:
                    if k != i and k != j:
                        if m[i][k] != 0 and m[i][k] == m[k][j]:
                            m[i][j] = m[i][k]
    result = 0
    for i in m:
        for j in i:
            if j == 0:
                break
        else:
            result +=1
    return result


if __name__ == "__main__":
    print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
    s = "abcdef"
    print(s[(len(s)-1)//2:len(s)//2+1])
