import sys

def floyd(n, edges):
    dist = [[sys.maxsize] * n for i in range(n)]
    next_node = [[-1] * n for i in range(n)]
    for u, v, w in edges:
        # if undirected graph
        dist[u][v] = w
        dist[v][u] = w
        next_node[u][v] = v
        next_node[v][u] = u
    for v in range(n):
        dist[v][v] = 0
        next_node[v][v] = v
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]
    return next_node


if __name__ == "__main__":
    print(floyd(4, [(0, 1, 5), (0, 3, 10), (3, 2, 1), (1, 2, 3)]))
