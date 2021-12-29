def solution(progresses, speeds):
    answer = []
    temp = [0] * len(progresses)
    for seq, i in enumerate(progresses):
        k = 100 - i
        if k % speeds[seq] == 0:
            temp[seq] = k // speeds[seq]
        else:
            temp[seq] = k // speeds[seq] + 1
    count = 1
    for i in range(1, len(progresses)):
        if temp[i-1] < temp[i]:
            answer.append(count)
            count = 1
        else:
            temp[i] = temp[i-1]
            count += 1
    answer.append(count)
    return answer

if __name__ == "__main__":
    solution([93, 30, 55], 	[1, 30, 5])