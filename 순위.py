def solution(n, results):
    graph = [[-1] * n for i in range(n)]
    for i, j in results:
        graph[i - 1][j - 1] = 1
        graph[j - 1][i - 1] = 0
    print(graph)
    return


if __name__ == "__main__":
    print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
