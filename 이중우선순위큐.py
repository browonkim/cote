from heapq import *

def solution(operations):
    maximum_heap = []
    minimum_heap = []
    for i in operations:
        if i[0] == "I":
            heappush(maximum_heap, -int(i[2:]))
            heappush(minimum_heap, int(i[2:]))
        else:
            if len(maximum_heap) == 0:
                continue
            if i[2] == "-":
                a = heappop(minimum_heap)
                for seq, num in enumerate(maximum_heap):
                    if num == -a:
                        maximum_heap.pop(seq)
                        break
            else:
                a = heappop(maximum_heap)
                for seq, num in enumerate(minimum_heap):
                    if num == -a:
                        minimum_heap.pop(seq)
                        break

    if len(maximum_heap) == 0:
        return [0, 0]
    else:
        return [-heappop(maximum_heap), heappop(minimum_heap)]


if __name__ == "__main__":
    print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
