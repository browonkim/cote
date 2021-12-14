def solution(n, computers):
    # 연결 찾기
    li = [-1] * n

    def find_root(k):
        if li[k] < 0:
            return k
        else:
            return find_root(li[k])

    for i in range(0, n):
        for j in range(i + 1, n):
            if computers[i][j] == 1:
                temp_i = find_root(i)
                temp_j = find_root(j)
                if temp_i == temp_j:
                    continue
                elif li[temp_i] <= li[temp_j]:
                    li[temp_i] += li[temp_j]
                    li[temp_j] = temp_i
                else:
                    li[temp_j] += li[temp_i]
                    li[temp_i] = temp_j

    print(li)
    t = [i for i in li if i < 0]
    return len(t)

if __name__ == "__main__":
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
