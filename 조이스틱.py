def solution(name: str):
    total_length = len(name)
    num_of_not_a = 0
    changes = 0
    for i in name:
        if i != 'A':
            num_of_not_a += 1
            changes += ord(i) - ord('A') if ord(i) - ord('A') < ord('Z') + 1 - ord(i) else ord('Z') + 1 - ord(i)

    def find_nearest(index: int):
        def if_same(c, f_i, b_i):
            if c == num_of_not_a:
                return f_cur, forward
            else:
                f, b = 1, 1
                while name[(f_i + f) % total_length] == 'A':
                    f += 1
                while name[b_i - b] == 'A':
                    b += 1
                if f > b:
                    return f_cur, forward
                elif f < b:
                    return b_cur, backward
                else:
                    return if_same(c + 1, (f_i + f) % total_length, b_i - b)

        f_cur, forward = (index + 1) % total_length, 1
        while name[f_cur] == 'A':
            f_cur = (f_cur + 1) % total_length
            forward += 1
        b_cur, backward = index - 1, 1
        while name[b_cur] == 'A':
            b_cur -= 1
            backward += 1
        b_cur = total_length + b_cur if b_cur < 0 else b_cur
        if forward < backward:
            return f_cur, forward
        elif forward > backward:
            return b_cur, backward
        else:
            return if_same(count + 1, f_cur, b_cur)

    count, moves, now = 0, 0, 0
    if name[0] != 'A':
        name = 'A' + name[1:]
        num_of_not_a -= 1

    while count < num_of_not_a:
        temp = find_nearest(now)
        print(temp)
        now = temp[0]
        moves += temp[1]
        count += 1
        name = name[:temp[0]] + 'A' + name[temp[0] + 1:]

    return changes + moves


if __name__ == "__main__":
    # print(ord('Z'))
    print(solution("BBABAAAB"))
