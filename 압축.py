def solution(msg):
    # initiate
    answer = []
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dictionary = {}
    for seq, word in enumerate(alphabets):
        dictionary[word] = seq+1
    seq = len(alphabets)+1
    # running
    # 현재 position(init=0)의 문자로 시작되는 substring 중에서 최대 길이의 문자열을 찾아냄
    i = 0
    while i < len(msg):
        j = i
        temp = prev = msg[i]
        flag = False
        while temp in dictionary:
            prev = temp
            j += 1
            if j < len(msg):
                temp += msg[j]
            else:
                flag = True
                break
        answer.append(dictionary[prev])
        if flag:
            if temp not in dictionary:
                dictionary[temp] = seq
                seq += 1
        else:
            dictionary[temp] = seq
            seq += 1
        i = j
    return answer

if __name__ == "__main__":
    print(solution("KAKAO"))