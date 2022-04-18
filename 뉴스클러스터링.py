from collections import Counter


def solution(str1, str2):
    def jak(a: list, b: list):
        if len(a) == 0 and len(b) == 0:
            return 1
        s = set()
        s.update(a)
        s.update(b)
        s1 = Counter(a)
        s2 = Counter(b)
        union, intersection = 0, 0
        for i in s:
            if i not in s1:
                union += s2[i]
            elif i not in s2:
                union += s1[i]
            else:
                union += s1[i] if s1[i] > s2[i] else s2[i]
                intersection += s1[i] if s1[i] < s2[i] else s2[i]
        return intersection / union

    li1, li2 = [], []
    for x, y in zip(str1, str1[1:]):
        if x.isalpha() and y.isalpha():
            li1.append(x.upper() + y.upper())
    for x, y in zip(str2, str2[1:]):
        if x.isalpha() and y.isalpha():
            li2.append(x.upper() + y.upper())
    return int(jak(li1, li2) * 65536)


if __name__ == "__main__":
    solution("aa1+aa2", "AAAA12")
