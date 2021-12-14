def solution(arr):
    """
    최소공배수는 LCM(Least Common Multiple), 최대공약수는 GCD(Greatest Common Divisor)
    최소공배수 = 두 수의 곱 / 두 수의 최대 공약수
    최대공약수 <- Euclidean Algorithm 사용하기
    :param arr: 숫자들을 담고 있는 리스트
    :return: 숫자들의 최소공배수
    """
    result = 1
    for i in arr:
        a, b = result, i
        while b != 0:
            a, b = b, a % b
        result = result * i // a
    return result


if __name__ == "__main__":
    print(solution([2, 6, 8, 14]))
