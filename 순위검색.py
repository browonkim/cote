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


from heapq import *


def solution2(info, query):
    lang = {"cpp": 0, "java": 1, "python": 2}
    pos = {"backend": 0, "frontend": 1}
    car = {"junior": 0, "senior": 1}
    food = {"chicken": 0, "pizza": 1}
    my_list = [[[[[], []], [[], []]], [[[], []], [[], []]]], [[[[], []], [[], []]], [[[], []], [[], []]]],
               [[[[], []], [[], []]], [[[], []], [[], []]]]]
    ranges = [0, 1, 2, 3]
    for i in info:
        temp = i.split()
        my_list[lang[temp[0]]][pos[temp[1]]][car[temp[2]]][food[temp[3]]].append(int(temp[4]))
    for i in my_list:
        for j in i:
            for k in j:
                for t in k:
                    t.sort()

    answer = []
    directory = [lang, pos, car, food]
    for i in query:
        count = 0
        s = i.split("and")
        q = []
        for t in s:
            q += t.split()
        indices = [[], [], [], []]
        lower = int(q[4])
        # q는 반복문 안의 로컬변수로 분리된 query의 요소들을 담고 있음.
        # q의 크기는 무조건 5개임.
        # 각각에 대해 indices += [directory[i][t[i]]]를 하든가 아니면 +=directory[i].values()
        for j in range(4):
            if q[j] == '-':
                indices[j] += directory[j].values()
            else:
                indices[j] += [directory[j][q[j]]]
        # 그리고나서 for i in indices[0]: for j in indices[1]: for k in indices[2] ... : for m in indices[4]: find(m)수행
        # count += find(m) 하기
        for i1 in indices[0]:
            for i2 in indices[1]:
                for i3 in indices[2]:
                    for i4 in indices[3]:
                        count += find(my_list[i1][i2][i3][i4], lower)
        answer.append(count)
        # 끝에 answer.append(count)하기
    return answer


def find(li, bound):
    if len(li) == 0:
        return 0
    if len(li) == 1:
        return 1 if li[0] >= bound else 0
    left = 0
    right = len(li)
    while left < right:
        median = (left + right) // 2
        if li[median] >= bound:
            right = median
        else:
            left = median + 1
    return len(li) - left


if __name__ == "__main__":
    print(solution2(
        ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
         "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
        , ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
           "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
           "- and - and - and - 150"]))

    print(find([1, 2, 3, 4, 5, 11, 12, 14, 354, 556, 999], 10))
