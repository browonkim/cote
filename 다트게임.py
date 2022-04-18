import re

def solution(dartResult):
    def convert(s):
        a = 1 if s[-1] == "S" else 2 if s[-1] == "D" else 3
        return int(s[0:-1]) ** a
    p = re.compile('[0-9]*[SDT]|[#*]')
    li = p.findall(dartResult)
    answer = []
    for token in li:
        if token == '*':
            if len(answer) > 1:
                answer[-2] *= 2
            answer[-1] *= 2
        elif token == '#':
            answer[-1] = -answer[-1]
        else:
            answer.append(convert(token))
    return sum(answer)

if __name__ == "__main__":
    print(solution("1D2S#10S"))