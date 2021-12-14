def solution(rows, columns, queries):
    result = []
    m = [[x + columns * y + 1 for x in range(columns)] for y in range(rows)]
    for q in queries:
        x1, y1, x2, y2 = q[0]-1, q[1]-1, q[2]-1, q[3]-1
        register = minimum = m[x1][y1]
        for i in range(y1+1, y2+1):
            register, m[x1][i] = m[x1][i], register
            minimum = register if register < minimum else minimum
        for i in range(x1+1, x2+1):
            register, m[i][y2] = m[i][y2], register
            minimum = register if register < minimum else minimum
        for i in range(y2-1, y1-1, -1):
            register, m[x2][i] = m[x2][i], register
            minimum = register if register < minimum else minimum
        for i in range(x2-1, x1-1, -1):
            register, m[i][y1] = m[i][y1], register
            minimum = register if register < minimum else minimum
        result.append(minimum)
    return result


if __name__ == "__main__":
    print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
