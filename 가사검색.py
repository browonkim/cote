from typing import List

def lower_bound_search(sorted_list: list, value):
    # 같은 값 중에서 가장 첫번째로 나오는 값. 같은 값이 없다면 큰 값 중에서 가장 작은 (첫번째로 나오는 값)
    left, right = 0, len(sorted_list)
    # print(sorted_list)
    # print(value)
    while left < right:
        median = (left + right) // 2
        # print("lower_bound" + str(median))
        if sorted_list[median].startswith(value) or value < sorted_list[median]:
            right = median
        else:
            left = median + 1
    return left


def upper_bound_search(sorted_list: list, value):
    # 큰 값 중에서 가장 작은 값. 같은 값이 있어도 큰 값 중에 가장 작은 값
    left, right = 0, len(sorted_list)
    # print(sorted_list)
    # print(value)
    while left < right:
        median = (left + right) // 2
        # print("upper_bound" + str(median))
        if sorted_list[median].startswith(value):
            left = median + 1
        elif value < sorted_list[median]:
            right = median
        else:
            left = median + 1
    return left

def solution(words: List[str], queries):
    answer = []
    prefixes = sorted(words)
    postfixes = sorted([x[::-1] for x in words])

    def find(position, key, length):
        if position == "prefix":
            start = lower_bound_search(prefixes, key)
            end = upper_bound_search(prefixes, key)
            # print("start: " + str(start) + " end: " + str(end))
            return len([x for x in prefixes[start:end] if len(x) == length])
        else:
            start = lower_bound_search(postfixes, key)
            end = upper_bound_search(postfixes, key)
            # print("start: " + str(start) + " end: " + str(end))
            return len([x for x in postfixes[start:end] if len(x) == length])
    for query in queries:
        query_length = len(query)
        if query[-1] == "?":
            answer.append(find("prefix", "".join(query.split('?')), query_length))
        elif query[0] == "?":
            answer.append(find("postfix", "".join(query.split('?'))[::-1], query_length))

    return answer


if __name__ == "__main__":
   test = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
   queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
   print(solution(test, queries))
