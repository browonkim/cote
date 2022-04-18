from heapq import *


def solution(n, works):
    # print(works)
    li = [-x for x in works]
    heapify(li)
    # print(works)
    for i in range(n):
        k = heappop(li)
        k += 1
        heappush(li, k)
    answer = 0
    for k in li:
        answer += k * k
    return answer


if __name__ == '__main__':
    print(solution(1, [1,2 ,2 ]))
