def minTime(files: list, numCores: int, limit: int):
    files.sort(reverse=True)
    count = 0
    result = 0
    for i in files:
        if count < limit and i % numCores == 0:
            result += i // numCores
            count += 1
        else:
            result += i
    return result


def maxCost(cost: list, labels: list, dailyCount: int):
    count = 0
    maxcost = 0
    sum = 0
    for c, l in zip(cost, labels):
        sum += c
        if l == "legal":
            count += 1
            if count == dailyCount:
                maxcost = maxcost if maxcost > sum else sum
                sum = 0
                count = 0
    return maxcost


def maxElement(n: int, maxSum: int, k: int):
    if n == maxSum:
        return 1
    if n + 1 > maxSum:
        return 1
    if n + 1 == maxSum:
        return 2
    sum_of_all = n + 1
    left, right = k, n - k - 1
    c = 1
    while True:
        sum_of_all += (1 + (c if c < left else left) + (c if c < right else right))
        if sum_of_all > maxSum:
            return c + 1
        c += 1


def minOperations(arr: list, threshold: int, d: int):
    def compare(a, b, op, k):
        if a > b:
            a = a // d
            op += k
        elif a < b:
            b = b // d
            op += 1
        else:
            return a, op
        return compare(a, b, op, k)

    arr.sort()
    length = len(arr)
    l = [arr[i:i + threshold] for i in range(length - threshold + 1)]
    minimum = int(float("inf"))
    for i in l:
        temp = i[0]
        result = 0
        for k in range(1, d):
            temp, tempresult = compare(temp, i[k], 0, k)
            result += tempresult
        minimum = minimum if minimum < result else result
    return minimum


def measure_distance(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def sort_points(points):
    def measure_distance(a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

    length = len(points)
    distances = [0] * length
    for i in range(length):
        for j in range(i, length):
            distance = measure_distance(points[i], points[j])
            distances[i] += distance
            distances[j] += distance
    print()
    return [points[i[0]] for i in sorted(list(enumerate(distances)), key=lambda a: a[1])]



if __name__ == "__main__":
        a = sort_points(
            [(-5, 3), (-1, 4), (8, 2), (2, 8), (7, 7), (0, 1), (9, 9), (3, 6), (1, 1), (20, 20), (-10, 3), (-2, -9),
             (2, -10), ])
        t = [[measure_distance(j, i) for i in a] for j in a]
        for i in t:
            print(i)
        print(sort_points([]))
        print(sort_points([]))
        print(sort_points([]))
        print(sort_points([]))
        print(sort_points([]))
        print(sort_points([]))
