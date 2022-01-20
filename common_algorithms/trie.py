from typing import List


class Trie_node:
    def __init__(self):
        self.children = {}
        self.num_of_children = 0


class Trie:
    def __init__(self):
        self.root = Trie_node()

    def insert(self, string):
        cur = self.root
        length = len(string)
        for character in string:
            cur.num_of_children += 1
            if character not in cur.children:
                cur.children[character] = Trie_node()
            cur = cur.children[character]

    def get_query_result(self, query: str):
        cur = self.root
        string = query.split('?')[0]
        for character in string:
            if character not in cur.children:
                return 0
            cur = cur.children[character]
        return cur.num_of_children


def solution(words: List[str], queries: List[str]):
    answer = []
    tries = {}
    for word in words:
        if len(word) not in tries:
            tries[len(word)] = (Trie(), Trie())
        tries[len(word)][0].insert(word)
        tries[len(word)][1].insert(word[::-1])
    for query in queries:
        if len(query) not in tries:
            answer.append(0)
        elif query[0] == '?':
            answer.append(tries[len(query)][1].get_query_result(query[::-1]))
        else:
            answer.append(tries[len(query)][0].get_query_result(query))
    return answer


if __name__ == "__main__":
    print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao", "froooooooo"],
                   ["fro??", "????o", "?????", "fro???", "pro?"]))
