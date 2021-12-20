def solution(n: int, r: list):
    routes = [[0 if j == i else -1 for j in range(n)] for i in range(n)]
    weights = [[0 if j == i else -1 for j in range(n)] for i in range(n)]

    # initialize
    for i in r:
        routes[i[0] - 1][i[1] - 1] = i[2]
        routes[i[1] - 1][i[0] - 1] = i[2]

    def dfs(start, dest, log, weight):
        if start == dest:
            return weight
        for seq, i in enumerate(routes[start]):
            a = False
            if i > 0 and seq not in log:
                a = dfs(seq, dest, log + [start], weight + routes[start][seq])
                if a:
                    return a
        else:
            return False

    for i in range(n):
        for j in range(i, n):
            weights[i][j] = dfs(i, j, [], 0)
            weights[j][i] = weights[i][j]

    result = [0] * n
    for i in range(n):
        for j in range(n):
            result[i] += weights[j][i]

    m = min(result)

    result_string = " "
    for seq, i in enumerate(result):
        if i == m:
            result_string += str(seq + 1) + " " + str(m) + " "

    return result_string


if __name__ == "__main__":
    print("#1" +
          solution(10,
                   [(1, 4, 4), (2, 4, 5), (3, 4, 3), (5, 4, 1), (4, 6, 10), (7, 6, 2), (9, 8, 3), (10, 8, 1),
                    (6, 8, 5)]))
