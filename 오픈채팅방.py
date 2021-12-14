def solution(record: list):
    result = {}
    answer = []
    for i in record:
        t = i.split()
        if t[0] != "Leave":
            result[t[1]] = t[2]
        answer = []
    for i in record:
        t = i.split(" ")
        if t[0] == "Enter":
            answer.append(result[t[1]] + "님이 들어왔습니다.")
        elif t[0] == "Leave":
            answer.append(result[t[1]] + "님이 나갔습니다.")
    return answer

if __name__ == "__main__":
    print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))