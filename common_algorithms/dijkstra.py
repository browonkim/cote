import sys
from heapq import *
class Graph:
    def __init__(self, num_of_vertices: int):
        self.v = num_of_vertices
        self.graph = [[0] * num_of_vertices for row in range(num_of_vertices)]

    def min_distance(self, distance: list, sets: list):
        minimum = sys.maxsize
        min_index = -1
        for u in range(self.v):
            if distance[u] < min and not sets[u]:
                minimum = distance[u]
                min_index = u
        return min_index

    def dijkstra(self, source: int):
        dist = [sys.maxsize] * self.v
        dist[source] = 0
        sets = [False] * self.v
        for target in range(self.v):
            x = self.min_distance(dist, sets)
            sets[x] = True
            for y in range(self.v):
                if self.graph[x][y] > 0 and not sets[y] and dist[y] > (dist[x] + self.graph[x][y]):
                    dist[y] = dist[x] + self.graph[x][y]
