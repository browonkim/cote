def bestSumAnyTreePath(parent, values):
    n = len(parent)
    children = {}
    for i in range(n):
        if parent[i] not in children:
            children[parent[i]] = [i]
        else:
            children[parent[i]].append(i)
    maximum = values[0]

    def travel(cur, total, todo):
        nonlocal maximum
        total += values[cur]
        maximum = max(total, maximum)
        if cur not in children or False not in todo:
            todo[cur] = False
            return
        for child in children[cur]:
            if todo[child]:
                continue
            todo[child] = True
            travel(child, total, todo)
        if parent[cur] != -1 and not todo[parent[cur]]:
            todo[parent[cur]] = True
            travel(parent[cur], total, todo)
        todo[cur] = False

    for i in range(n):
        travel(i, 0, [False if k != i else True for k in range(n)])
    return maximum

if __name__ == '__main__':
    print(bestSumAnyTreePath([-1,0,1,2,0],[-2,10,10,-3,10]))