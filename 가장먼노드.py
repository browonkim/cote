from collections import deque
def solution(n, edge):
    answer = [1] + [0] * (n - 1)
    route = [[] for i in range(n)]
    q = deque([0])
    for i in edge:
        route[i[0]-1].append(i[1]-1)
        route[i[1]-1].append(i[0]-1)
    while q:
        l = len(q)
        for i in range(l):
            node = q.popleft()
            for e in route[node]:
                if answer[e] == 0:
                    answer[e] = 1
                    q.append(e)
    return l

if __name__ == "__main__":
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
