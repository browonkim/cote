def solution(numbers):
    def logic(n):
        s = bin(n)[2:]
        if s[-1] == '0':
            return s[:-1] + '1'
        else:
            s = s[::-1]
            for seq, bit in enumerate(s):
                if bit == '0':
                    s = s[:seq - 1] + '01' + s[seq + 1:]
                    return s[::-1]
            return (s[:-1] + '01')[::-1]
    return [int(logic(x), 2) for x in numbers]


if __name__ == '__main__':
    print(solution([2, 7]))
