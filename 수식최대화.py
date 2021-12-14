import itertools
def solution(expression):
    answer = 0
    a = ['+', '-', '*']
    priority = list(itertools.permutations(a, 3))
    tokens = []
    temp = ""
    for t in expression:
        if t.isdecimal():
            temp += t
        else:
            tokens.append(int(temp))
            temp = ""
            tokens.append(t)
    tokens.append(int(temp))
    for i in priority:
        stack = []
        result = []
        for op in tokens:
            if type(op) is int:
                result.append(op)
            else:
                if len(stack) == 0:
                    stack.append(op)
                else:
                    while len(stack) != 0 and i.index(stack[-1]) <= i.index(op):
                        result.append(stack.pop())
                    stack.append(op)
        result += reversed(stack)
        t = []
        for op in result:
            if type(op) is int:
                t.append(op)
            else:
                a = t.pop()
                b = t.pop()
                if op == "-":
                    t.append(b-a)
                elif op == "+":
                    t.append(a+b)
                elif op == "*":
                    t.append(a*b)
        tmp = abs(t.pop())
        answer = answer if answer > tmp else tmp
    return answer


if __name__ == "__main__":
    print(solution("100-200*300-500+20"))