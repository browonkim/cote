import sys


def quiz2(points: list):
    pass


class SimpleTextEditor:
    def __init__(self):
        self.S = ""
        self.log = []
        self.functions = [self.append, self.delete, self.printing, self.undo]

    def getfunc(self, index, *args):
        if index == 3:
            self.functions[3]()
        else:
            self.functions[index](args[0] if index == 0 else int(args[0]))

    def logging(self, cur):
        self.log.append(cur)

    def append(self, w):
        self.S += w
        self.logging(self.S)

    def delete(self, k):
        self.S = self.S[:-k]
        self.logging(self.S)

    def printing(self, k):
        print(self.S[k-1])

    def undo(self):
        self.log.pop(-1)
        self.S = self.log[-1]


if __name__ == "__main__":
    q = int(sys.stdin.readline())
    a = SimpleTextEditor()
    for i in range(q):
        s = sys.stdin.readline().strip().split()
        function_index, function_param = int(s[0]), None if len(s) <= 1 else s[1]
        a.getfunc(function_index-1, function_param)
