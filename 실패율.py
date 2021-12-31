def solution(N, stages):
    mydict, result, sum = {}, {}, 0
    for i in stages:
        if i not in mydict:
            if i == N + 1:
                sum += 1
            else:
                mydict[i] = 1
        else:
            mydict[i] += 1
    for i in range(N, 0, -1):
        if i not in mydict:
            result[i] = 0
        else:
            sum += mydict[i]
            result[i] = mydict[i] / sum
    return [-t[1] for t in (sorted([(y, -x) for x, y in result.items()], reverse=True))]
from itertools import c


if __name__ == "__main__":
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
