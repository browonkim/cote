def deprecated_solution(phone_book):
    length = len(phone_book)
    for i in range(0, length):
        for j in range(i + 1, length):
            if len(phone_book[i]) < len(phone_book[j]):
                s1, s2 = phone_book[i], phone_book[j][0:len(phone_book[i])]
            else:
                s1, s2 = phone_book[i][0:len(phone_book[j])], phone_book[j]
            if s1 == s2:
                return False
    return True


def solution(phone_book):
    p = {}
    maximum = 0
    for i in phone_book:
        for j in range(1, maximum):
            if i[:i] in p:
                return False
        maximum = len(i) if len(i) > maximum else maximum
        p[i] = True
    return True
