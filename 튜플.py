import re


def solution(s: str):
    li = [y.split(',') for y in [x for x in re.split('{|}', s[1:-1]) if x != ',' and x != '']]
    li.sort(key= lambda x: len(x))
    comp = set()
    result = []
    for sublist in li:
        for i in sublist:
            if i not in comp:
                result.append(int(i))
                comp.add(i)
                break
    return result


if __name__ == "__main__":
    print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))

