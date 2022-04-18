import math


def getMaxBarrier(initialEnergy, th):
    # # Write your code here
    l = len(initialEnergy)
    sof = sum([i for i in initialEnergy if i > 0])
    n = 0
    initialEnergy.sort()
    print(sof)
    for seq, i in enumerate(initialEnergy):
        if i < 0:
            continue
        if sof - (l - seq) * i < th:
            return n + math.ceil((sof-th)/(l-seq))
        elif sof - (l - seq) * i == th:
            return n + i
        else:
            n += i
            sof -= (l - seq) * i
        print(sof)
    return n


if __name__ == '__main__':
    print(getMaxBarrier([5,2,13,10], 8))
