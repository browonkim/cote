def solution(arr):
    prev = None

    def comp(n):
        nonlocal prev
        prev, result = n, prev
        return prev

    return [x for x in arr if x != comp(x)]


def s(s):
    def convert(substring):
        return ''.join([x.upper() if seq % 2 == 0 else x.lower() for seq, x in enumerate(substring)])
    stack, li = "", []
    for x in s:
        if x == " ":
            li += [stack, x]
            stack = ""
        else:
            stack += x
    li.append(stack)
    print(li)
    return ''.join(map(convert, li))


if __name__ == "__main__":
    print(s("try hello world"))