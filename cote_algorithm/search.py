def search(sorted_list: list, value):
    left, right = 0, len(sorted_list)
    while left < right:
        median = (left + right) // 2
        if value < sorted_list[median]:
            right = median
        elif value > sorted_list[median]:
            left = median + 1
        else:
            return median


def lower_bound(sorted_list: list, value):
    # 같은 값 중에서 가장 첫번째로 나오는 값. 같은 값이 없다면 큰 값 중에서 가장 작은 (첫번째로 나오는 값)
    left, right = 0, len(sorted_list)
    while left < right:
        median = (left + right) // 2
        if value <= sorted_list[median]:
            right = median
        else:
            left = median + 1
    return left


def upper_bound(sorted_list: list, value):
    # 큰 값 중에서 가장 작은 값. 같은 값이 있어도 큰 값 중에 가장 작은 값
    left, right = 0, len(sorted_list)
    while left < right:
        median = (left + right) // 2
        if value < sorted_list[median]:
            right = median
        else:
            left = median + 1
    return left

def quick_sort(unsorted_list: list):
    pass


if __name__ == "__main__":
    print(lower_bound([1, 2, 4, 7, 8, 9, 10, 22, 35, 36, 38, 44, 44, 44, 45, 55], 44))
