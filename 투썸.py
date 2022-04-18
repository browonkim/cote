def solution(arr):
    recent = {}
    dict_for_duplication = {}
    for index, person in enumerate(arr):
        if person not in recent:
            recent[person] = index
        else:
            if person not in dict_for_duplication:
                dict_for_duplication[person] = index - recent[person]
            else:
                dict_for_duplication[person] = min(dict_for_duplication[person], index - recent[person])
            recent[person] = index
    return min(dict_for_duplication.values()) if len(dict_for_duplication) != 0 else -1

if __name__ == '__main__':
    print(solution([2, 1, 3, 1, 4, 2, 1, 3]))