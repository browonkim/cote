def solution(gems):

    def resolve(s: list, front: int):
        size = len(s)
        i = 0
        while i < size and s[i] in s[i+1:]:
            i += 1
            front += 1
        s = s[i:]
        return front

    gemset = set()
    gemset.update(gems)
    count, goal = set(), len(gemset)
    dequeue = []
    minimum = 10000000
    left, right = 0, 0
    for seq, gem in enumerate(gems):
        dequeue.append(gem)
        count.add(gem)
        temp = resolve(dequeue, left)
        if len(count) == goal:
            if minimum > len(dequeue):
                minimum = len(dequeue)
                right = seq
                left = temp

    return [left+1, right+1]

if __name__ == "__main__":
    print(solution((["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])))