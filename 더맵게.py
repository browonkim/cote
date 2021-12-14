from heapq import *

def solution(scoville, K):
    p = []
    for i in scoville:
        heappush(p, i)
    temp = heappop(p)
    if temp >= K:
        return 0
    answer = 0
    while temp < K:
        if len(p) < 1:
            return -1
        temp += heappop(p) * 2
        heappush(p, temp)
        temp = heappop(p)
        answer += 1
    return answer


if __name__ == "__main__":
    solution([1, 2, 3, 9, 10, 12],	7)