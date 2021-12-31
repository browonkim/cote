def solution(gems):
    box = {}
    left, right = 0, 0
    min_left, min_right = 0, len(gems)
    for seq, gem in enumerate(gems):
        right = seq
        if gem not in box:
            box[gem] = 1
            min_left, min_right = left, right
        else:
            box[gem] += 1
            while box[gems[left]] > 1 and left <= right:
                box[gems[left]] -= 1
                left += 1
            if min_right - min_left + 1 > right - left + 1:
                min_right, min_left = right, left
    return [min_left + 1, min_right + 1]


if __name__ == "__main__":
    print(solution((["XYZ", "XYZ", "XYZ"])))
