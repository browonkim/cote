def solution(maps):
    answer = 0
    row, col = len(maps), len(maps[0])
    me, target = (0, 0), (row - 1, col - 1)
    queue = [(0, 0, 0)]
    min_distance = row * col

    def travel(n):
        nonlocal min_distance
        if len(queue) == 0:
            return -1
        pos = queue.pop(0)
        if (pos[0], pos[1]) == target:
            min_distance = min(min_distance, pos[2])
        '''
        block 된 부분 제외하기 +
        방문했던 부분 제외하기 << 이게 어렵다
        '''
    return min_distance
