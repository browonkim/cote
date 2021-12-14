def solution(progresses, speeds):
    prev = (100 - progresses[0]) // speeds[0] if (100 - progresses[0]) % speeds[0] == 0 else (100 - progresses[
            0]) // speeds[0] + 1
    answer = [1]
    for i in range(1, len(progresses)):
        temp = (100 - progresses[i]) // speeds[i] if (100 - progresses[i]) % speeds[i] == 0 else (100 - progresses[
            i]) // speeds[i] + 1
        if prev >= temp:
            answer[-1] += 1
        else:
            prev = temp
            answer.append(1)
    return answer
