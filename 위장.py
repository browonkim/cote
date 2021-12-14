def solution(clothes):
    answer = 1
    closet = {}
    for i, j in clothes:
        if j not in closet:
            closet[j] = 1
        else:
            closet[j] += 1
    for i in closet.values():
        answer *= i+1
    return answer -1


if __name__ == "__main__":
    print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
