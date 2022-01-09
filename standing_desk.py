def left(cur, mat, m, w):
    for k in range(w):
        if mat[cur[0]][cur[1]]:
            if cur[1] - 1 < 0 and k < w - 1:
                break
            else:
                if k < w - 1:
                    cur[1] -= 1
        else:
            break
    else:
        return cur
    return False


def right(cur, mat, m, w):
    for k in range(w):
        if mat[cur[0]][cur[1]]:
            if cur[1] + 1 >= m and k < w - 1:
                break
            else:
                if k < w - 1:
                    cur[1] += 1
        else:
            break
    else:
        return cur
    return False


def up(cur, mat, n, h):
    for k in range(h):
        if mat[cur[0]][cur[1]]:
            if cur[0] - 1 < 0 and k < h - 1:
                break
            else:
                if k < h - 1:
                    cur[0] -= 1
        else:
            break
    else:
        return cur
    return False


def down(cur, mat, n, h):
    for k in range(h):
        if mat[cur[0]][cur[1]]:
            if cur[0] + 1 >= n and k < h - 1:
                break
            else:
                if k < h - 1:
                    cur[0] += 1
        else:
            break
    else:
        return cur
    return False


def solution(isAvailable, N, M, H, W):
    answer = 0
    funcs = [[left, down, right], [right, down, left], [up, left, down], [down, left, up]]
    
    for i in range(N):
        for j in range(M):
            for seq, func in enumerate(funcs):
                cur = [i, j]
                cur = func[0](cur, isAvailable, N, M, H, W)
                print(func[0].__name__+ " "+ str(cur))
                if cur:
                    cur = func[1](cur, isAvailable, N, M, H, W)
                    print(func[1].__name__ + " "+str(cur))
                    if cur:
                        cur = func[2](cur, isAvailable, N, M, H, W)
                        print(func[2].__name__ +" "+ str(cur))
                        if cur:
                            print(str(i) + " + " + str(j))
                            answer += 1
    return answer

if __name__ == "__main__":
    print(solution(["1111", "1011", "1011", "1111"], 4, 4, 2, 3))