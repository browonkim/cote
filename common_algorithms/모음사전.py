def solution(word):
    d = {'A': 1, 'E': 2, 'I': 3, 'O': 4, 'U': 5}
    word = word.ljust(5)
    result = 0
    for seq, w in enumerate(word[::-1]):
        if w != " ":
            result += (d[w] - 1) * (6 ** seq) + 1
    return result

if __name__ == "__main__":
    print(solution("AAAI"))
