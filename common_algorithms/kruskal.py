from collections import defaultdict


def kruskal(edges: list):
    sets = {}

    def union(a, b):
        def find_root(key: int):
            if sets[key] < 0:
                return key
            else:
                return find_root(sets[key])

        a_root = find_root(a)
        b_root = find_root(b)
        if a_root == b_root:
            return True
        if sets[a_root] < sets[b_root]:
            sets[a_root] += sets[b_root]
            sets[b_root] = a_root
        else:
            sets[b_root] += sets[a_root]
            sets[a_root] = b_root
        return False

    edges.sort(key=lambda a: a[2])
    for i in edges:
        if i[0] not in sets:
            sets[i[0]] = -1
        if i[1] not in sets:
            sets[i[1]] = -1
    result, num_of_edges = [], 0
    for i in edges:
        if not union(i[0], i[1]):
            result.append(i)
            num_of_edges += 1
            if num_of_edges == len(sets.keys()) - 1:
                break
    return result


if __name__ == "__main__":
    print(kruskal([(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]))
