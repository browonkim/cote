class Node:
    def __init__(self, weight):
        self.children = []
        self.weight = weight

def solution(weights, edges):
    if sum(weights) != 0:
        return -1
    n_node = len(weights)
    nodes = {}
    neighbors = {}
    for i in range(n_node):
        nodes[i] = Node(weights[i])
    for u, v in edges:
        if u not in neighbors:
            neighbors[u] = []
        if v not in neighbors:
            neighbors[v] = []
        neighbors[u].append(v)
        neighbors[v].append(u)
    stack, exist = [0], set()
    while len(stack) > 0:
        cur = stack.pop()
        exist.add(cur)
        temp = [x for x in neighbors[cur] if x not in exist]
        stack += temp
        nodes[cur].children += temp
    count = 0

    def visit(n):
        nonlocal count
        for child in nodes[n].children:
            t = visit(child)
            nodes[n].weight += t
        result = nodes[n].weight
        count += abs(result)
        nodes[n].weight = 0
        return result

    visit(0)
    return count

if __name__ == "__main__":
    print(solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]]))
