
def solution(numbers):
    def comp(a, b):
        l_a, l_b = len(a), len(b)
        if l_a == l_b:
            return a < b
        elif l_a > l_b:
            temp = a[:l_b]
            if temp < b:
                return True
            elif temp > b:
                return False
            else:
                return comp(a[l_b:], b)
        else:
            temp = b[:l_a]
            if a < temp:
                return True
            elif a > temp:
                return False
            else:
                return comp(a, b[l_a:])

    class Compare:
        def __init__(self, key):
            self.key = key

        def __lt__(self, other):
            return comp(self.key, other.key)

    str_numbers = list(map(str, numbers))
    str_numbers.sort(key=Compare, reverse=True)
    return str(int("".join(str_numbers)))

if __name__ == "__main__":
    print(solution(	[3, 30, 34, 5, 9]))