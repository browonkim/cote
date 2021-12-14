def solution(begin, target, words):

    # TODO

    def compare(word1, word2):
        count = 0
        for i,j in word1,word2:
            if i==j:
                count +=1
                if count > 1:
                    return False
        return True

    queue = []
    # def dfs(cur, not_visited):
        # 방문 안한 문자열을 모두 방문할 것
        # 단 각 cur에 대해서 수행할 것
        # 진입하다가 언젠가 target과 동일한 지점을 찾기
        # 즉 compare==true이고 tartget과 같다면 중지. 근데 최소 지점을 찾아야함
        # 다시말해서 bfs로 구현해야함
    while len(queue) > 0:
        # pop front
        # push all of front
        pass

    answer = 0
    return answer

if __name__ == "__main__":
    pass
