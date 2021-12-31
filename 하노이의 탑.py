def solution(k):
    answer = []

    def hanoi(n, source, mid, target):
        if n == 1:
            answer.append([source, target])
            return
        hanoi(n - 1, source, target, mid)
        answer.append([source, target])
        hanoi(n - 1, mid, source, target)
        return

    hanoi(k, 1, 2, 3)
    return answer


if __name__ == "__main__":
    print(solution(15))
