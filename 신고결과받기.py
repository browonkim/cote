from functools import reduce

def solution(id_list, report: list, k):
    answer = []
    stacks = {}
    ids = {}
    repo = [x.split() for x in report]
    for i, rep in repo:
        if rep not in stacks:
            stacks[rep] = set()
        if i not in ids:
            ids[i] = set()
        stacks[rep].add(i)
        ids[i].add(rep)
    for i in id_list:
        if i not in ids:
            answer.append(0)
        else:
            answer.append(reduce(lambda x, y: x + 1 if y in stacks and len(stacks[y]) >= 2 else x, ids[i], 0))
    return answer
