def solution(citations: list):
    citations.sort(reverse=True)
    len_of_cit = len(citations)

    def find(a):
        for seq, i in enumerate(citations):
            if a == i:
                return seq
            elif a > i:
                return seq-1
        return 0

    maximum = 0
    for i in range(citations[0]):
        n = find(i) + 1
        if n >= i >= len_of_cit - i:
            maximum = maximum if maximum > i else i
    return maximum
