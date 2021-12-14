class Compare:
    def __init__(self, key):
        self.key = key
        key = key.upper()
        head = ""
        for i in key:
            if i.isdecimal():
                break
            else:
                head += i
        self.head = head
        number = ""
        s = 0
        count = False
        for i in key:
            if i.isdecimal():
                count = True
                number += i
                s += 1
                if s == 5:
                    break
            elif count:
                break
        self.number = int(number)

    def __lt__(self, other):
        if self.head == other.head:
            return self.number < other.number
        else:
            return self.head < other.head

def solution(files):

    return sorted(files, key=lambda key: Compare(key))


if __name__ == "__main__":
    li = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
    print(li)
    print(solution(li))
