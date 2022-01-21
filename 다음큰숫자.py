from collections import Counter


def solution(n):
    s = bin(n)[2:]
    before = Counter(s)['1']
    s = s[::-1]
    for seq, bit in enumerate(s):
        if bit == '1':
            n += 2 ** seq
            break
    s = bin(n)[2:][::-1]
    after = Counter(s)['1']
    for seq, bit in enumerate(s):
        if after >= before:
            break
        else:
            if s[seq] == '0':
                s = s[:seq] + '1' + s[seq + 1:]
                after += 1
    return int(s[::-1], 2)


if __name__ == "__main__":
    print(solution(78))
