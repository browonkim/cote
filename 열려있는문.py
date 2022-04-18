def solution(n):
    # 에라토스테네스의 체랑 비슷
    # if 0 it's closed else it's open
    li = [0] + [1] * n
    for i in range(2, (n // 2) + 1):
        for k in range(i, n + 1, i):
            li[k] = 0 if li[k] == 0 else 1
    return sum(li[:n//2+1]) + (n-n//2)-sum(li[n//2+1:])

