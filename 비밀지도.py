def solution(k, arr1, arr2):
    def to_binary(n):
        result = ""
        while n > 0:
            result += str(n % 2)
            n //= 2
        result = "".join(reversed(result))
        while len(result) != k:
            result = "0" + result
        return result
    answer = [[0] * k for i in range(k)]
    for i in range(k):
        ar1 = to_binary(arr1[i])
        ar2 = to_binary(arr2[i])
        for j in range(-1, -k-1, -1):
            answer[i][j] = ar1[j]
        for j in range(-1, -k-1, -1):
            answer[i][j] = int(ar2[j]) or int(answer[i][j])
    a = []
    for i in answer:
        temp = ""
        for j in i:
            temp += "#" if j else " "
        a.append(temp)
    return a

if __name__ == "__main__":
    print(solution(5,	[9, 20, 28, 18, 11], [30, 1, 21, 17, 28] ))
