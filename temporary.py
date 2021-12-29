def getTheGroups(n, queryType, students1, students2):
    # Write your code here
    answer = []
    mydict = {}

    def find_root(k):
        if mydict[k] < 0:
            return k
        else:
            return find_root(mydict[k])

    for seq, query in enumerate(queryType):
        if query == "Friend":
            if students1[seq] not in mydict:
                mydict[students1[seq]] = -1
            if students2[seq] not in mydict:
                mydict[students2[seq]] = -1
            temp_i = find_root(students1[seq])
            temp_j = find_root(students2[seq])
            if temp_i == temp_j:
                continue
            elif mydict[temp_i] <= mydict[temp_j]:
                mydict[temp_i] += mydict[temp_j]
                mydict[temp_j] = temp_i
            else:
                mydict[temp_j] += mydict[temp_i]
                mydict[temp_i] = temp_j
        else:
            if students2[seq] not in mydict:
                mydict[students2[seq]] = -1
            if students1[seq] not in mydict:
                mydict[students1[seq]] = -1
            temp = mydict[find_root(students2[seq])] + mydict[find_root(students1[seq])]
            answer.append(-temp)
    return answer