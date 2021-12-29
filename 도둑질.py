def solution(money: list):
    num_of_houses = len(money)
    if num_of_houses < 4:
        return max(money)
    elif num_of_houses == 4:
        return max(money[0]+money[2], money[1]+money[3])
    first = [i for i in money[:-1]]
    second = [i for i in money[1:]]
    third = [i for i in money[2:]]

    def optimize(li: list):
        size = len(li)
        if size < 3:
            return max(li[0], li[1])
        li[2] = max(li[0]+li[2], li[1])
        if size < 4:
            return li[2]
        li[3] = max(li[0]+li[3], li[1]+li[3], li[2])
        for i in range(4, size):
            li[i] = max(li[i]+li[i-2], li[i-1])
        return li[-1]

    return max(optimize(first), optimize(second), optimize(third))

if __name__ == "__main__":
    print(solution([1, 0, 0, 9, 324, 123, 14, 44, 1, 1, 354, 6, 9]))
