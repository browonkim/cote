from heapq import *
def dijkstra(m, source):
    visited = [False] * len(m)
    dist = {source: 0}
