def matches(open_bracket, close_bracket):
    return ord(open_bracket) + 2 == ord(close_bracket) or ord(open_bracket) + 1 == ord(close_bracket)


def solution(s):
    opens = {"[": 0, "{": 0, "(": 0}
    closes = {"]": 0, "}": 0, ")": 0}

    def stack_push(a):
        nonlocal opens, closes
        if a in opens:
            opens[a] += 1
        else:
            closes[a] += 1

    stack, result = [], 0
    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        # 빈공간에 추가 될 경우
        # 그냥 추가하기
        else:
            if stack[-1] in opens:
                if s[i] in closes:
                    if matches(stack[-1], s[i]):
                        if i == len(s) - 1 or s[i + 1] in opens:
                            result += 1
                        temp = stack.pop(-1)
                        if temp in opens:
                            opens[temp] -= 1
                        else:
                            closes[temp] -= 1
                    else:
                        return 0
                else:
                    stack.append(s[i])
                    stack_push(s[i])
            else:
                stack.append(s[i])
                stack_push(s[i])
        # 스택의 탑이 opens일 경우
        # 현재 문자가 closes 인 경우 match되면 ok
        # 이 때 해당 문자가 마지막이면 .즉 i가 len(s) - 1 이라면 그냥 1 추가하기
        # 이 때 해당 문자가 마지막이 아니면 다음 문자를 확인. 만약 다음 문자가 closes이면 그냥 pop만 시키기.
        # 해당 문자가 마지막이 아니고 다음 문자가 opens면 1 추가하기
        # close인데 match 안되면 return 0
        # 스택의 탑이 close인경우 (즉 else)
        # 그냥 추가해주기
    for i, j in zip(opens.values(), closes.values()):
        if i != j:
            return 0
    if len(stack) == 0:
        return result
    else:
        temp = []
        for i in stack:
            if len(temp) == 0:
                temp.append(i)
            else:
                if matches(i, temp[-1]):
                    temp.pop(-1)
                else:
                    temp.append(i)
        if len(temp) != 0:
            return 0
        else:
            return result + 1
    # 모든 문자에 대해 끝났으면 우선
    # opens.values 와 closes.values 가 match되는지 확인하기
    # 이제 stack을 검증해야함
    # stack이 비어있다면 return result
    # stack의 연산을 이번엔 역으로 할것. 단 이번에는 그냥 stack연산만 해주면 됨 (일반 괄호 문제처럼)
    # 최종적으로 stack이 0이되면 +1
    # stack이 비어있지않다면 return 0


if __name__ == "__main__":
    print(solution("{{{{()()}}}}"))
