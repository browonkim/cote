def solution(quotes):
    stack = []
    answer = [1] * len(quotes)
    for seq, i in enumerate(quotes):
        while len(stack) != 0 and quotes[stack[-1]] <= i:
            stack.pop(-1)
        if len(stack) == 0:
            stack.append(seq)
            answer[seq] = seq + 1
        else:
            answer[seq] = seq - stack[-1]
            stack.append(seq)
    return answer

if __name__ == "__main__":
    print(solution([7, 10, 8, 6, 3, 7, 8]))
