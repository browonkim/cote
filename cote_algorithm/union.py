"""
union 을 dictionary 로 구현했습니다. 다만, 연속된 배열로 선정하는게 더 유리할 경우 list 로 코드를 수정하면 됩니다.
이때 dictionary 의 key 가 list 의 index 가 되게 하면 됩니다.
"""


def union(items: list, joins: list):
    sets = {}

    def find_root_key_of_item(item_key):
        if sets[item_key] < 0:
            return item_key
        else:
            return find_root_key_of_item(sets[item_key])

    # initialize
    for item in items:
        sets[item] = -1

    # disjoint join
    # set size is negative integer
    for i, j in joins:
        root_of_i = find_root_key_of_item(i)
        root_of_j = find_root_key_of_item(j)
        i_set_size = sets[root_of_i]
        j_set_size = sets[root_of_j]
        if root_of_i == root_of_j:
            continue
        elif i_set_size <= j_set_size:
            sets[root_of_i] += j_set_size
            sets[root_of_j] = root_of_i
        else:
            sets[root_of_j] += i_set_size
            sets[root_of_i] = root_of_j

    # sets for human
    set_for_human = {}
    for key in sets.keys():
        root = find_root_key_of_item(key)
        if root in set_for_human:
            set_for_human[root].append(key)
        else:
            set_for_human[root] = [key]
    return set_for_human


if __name__ == "__main__":
    print(union(list(range(10)), [(1, 3), (2, 3), (1, 4), (5, 6), (7, 8), (1, 8)]))
