def solution(s):
    if len(s) == 0:
        return s
    u, v = "", ""
    stack = []
    flag = False
    for seq, i in enumerate(s):
        if len(stack) == 0:
            if i == '(':
                flag = True
            stack.append(i)
        elif stack[-1] == i:
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0:
                u, v = s[:seq+1], s[seq+1:]
                break
    else:
        u, v = s, ""
    if flag:
        return u + solution(v)
    else:
        u = u[1:-1]
        for seq, i in enumerate(u):
            if i == "(":
                u = u[:seq] + ")" + u[seq+1:]
            elif i == ")":
                u = u[:seq] + "(" + u[seq+1:]
        return "(" + solution(v) + ")" + "".join(u)

if __name__ == "__main__":
    print(solution("()))((()"))