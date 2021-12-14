def solution(info, query):
    info_list = [x.split() for x in info]
    print(info_list)
    answer = []
    for i in query:
        s = i.split("and")
        q = []
        for t in s:
            q += t.split()
        print(q)
        count = 0
        for x in info_list:
            if x[0] == q[0] or q[0] == "-":
                if x[1] == q[1] or q[1] == "-":
                    if x[2] == q[2] or q[2] == "-":
                        if x[3] == q[3] or q[3] == "-":
                            if int(x[4]) >= int(q[4]):
                                count += 1
        answer.append(count)
    return answer


if __name__ == "__main__":
    print(solution(
        ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
         "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
        , ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
           "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
           "- and - and - and - 150"]))
