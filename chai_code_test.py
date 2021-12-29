import sys

def getTheGroups(n, queryType, students1, students2):
    # Write your code here
    answer = [0] * n
    mydict = {}
    for seq, i in enumerate(queryType):
        if i == "Friend":
            if students1[seq] not in mydict:
                mydict[students1[seq]] = set()

            else:
                mydict[students1[seq]].update([students1[seq], students2[seq]])
            mydict[students2[seq]] = mydict[students1[seq]]
        else:
            answer[seq] = len(mydict[students1[seq]]) + len(mydict[students2[seq]])
    return answer


if __name__ == "__main__":
    q = int(sys.stdin.readline())
    for i in range(q):
        s = sys.stdin.readline().strip().split()
