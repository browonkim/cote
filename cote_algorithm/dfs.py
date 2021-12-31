def dfs(edges, n):
    routes = [[0] * n for i in range(n)]
    for src, des in edges:
        routes[src][des] = 1
        # if not digraph
        routes[des][src] = 1

    def travel(cur, visited):
        print(cur, end=" ")
        print(visited)
        if len(visited) == n:
            return True
        for seq, to in enumerate(routes[cur]):
            if to and seq not in visited:
                if travel(seq, visited + [seq]):
                    return True
        return False

    travel(0, [0])


if __name__ == "__main__":
    dfs([[0, 1], [0, 2], [1, 2], [2, 3], [3, 4], [4, 5], [4, 6], [5, 6]], 7)
