def solution(begin: str, target: str, words: list):
    if target not in words:
        return 0
    minimum = 0
    for i in range(len(begin)):
        if begin[i] != target[i]:
            minimum += 1
    target_seq = -1
    for seq, i in enumerate(words):
        if i == target:
            target_seq = seq + 1
            break
    words = [begin] + words
    num_of_words = len(words)
    len_of_word = len(words[0])
    routes = [[False] * num_of_words for i in words]
    for i in range(num_of_words):
        for j in range(i + 1, num_of_words):
            count = 0
            for k in range(len_of_word):
                if words[i][k] != words[j][k]:
                    count += 1
                    if count > 1:
                        break
            else:
                if count == 1:
                    routes[i][j], routes[j][i] = True, True

    def dfs(cur: int, visited: list):
        result = len_of_word*2
        if cur == target_seq:
            return len(visited) - 1
        for i, canGo in enumerate(routes[cur]):
            if canGo:
                if i not in visited:
                    temp = dfs(i, visited + [i])
                    if temp:
                        if temp == minimum:
                            return minimum
                        result = result if result < temp else temp
        else:
            if result < len_of_word*2:
                return result
            else:
                return False

    answer = dfs(0, [0])
    if answer:
        return answer
    else:
        return 0

if __name__ == "__main__":
    print(solution("hit",	"hhh"	,["hhh","hht"]))
