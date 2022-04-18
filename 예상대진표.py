def solution(n, m):
    count = 0
    while n != m:
        n = (n+1)//2
        m = (m+1)//2
        count += 1
    return count
