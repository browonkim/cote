import collections


def bfs(n, edges):
    routes = [[0] * n for i in range(n)]
    for src, des in edges:
        routes[src][des] = 1
        routes[des][src] = 1
    deq = collections.deque([0])
    visited = [False] * n
    while len(deq) > 0:
        cur = deq.popleft()
        print(cur)
        visited[cur] = True
        for seq, i in enumerate(routes[cur]):
            if i and not visited[seq]:
                deq.append(seq)
        for i in visited:
            if not i:
                break
        else:
            return


if __name__ == "__main__":
    bfs(7, [[0, 1], [0, 2], [1, 2], [2, 3], [3, 4], [4, 5], [4, 6], [5, 6]])
