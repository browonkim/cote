from itertools import combinations

def solution(orders, course):
    answer = []
    for c in course:
        counting = {}
        maximum = 1
        for o in orders:
            temp = list(o)
            temp.sort()
            order = "".join(temp)
            for tup in combinations(order, c):
                if tup in counting:
                    counting[tup] += 1
                else:
                    counting[tup] = 1
        for value in counting.values():
            maximum = value if maximum < value else maximum
        if maximum == 1:
            continue
        for key, value in counting.items():
            if value == maximum:
                answer.append("".join(key))
    answer.sort()
    return answer

if __name__ == "__main__":
    print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
