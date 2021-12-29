def solution(tickets):
    answer = []

    def dfs(start, left, visit):
        nonlocal answer
        if len(left) == 0:
            visit += [start]
            return visit
        for seq, ticket in enumerate(left):
            if ticket[0] == start:
                temp = dfs(ticket[1], left[:seq]+left[seq+1:], visit+[ticket[0]])
                if temp:
                    answer.append(temp)
        else:
            return False

    for s, i in enumerate(tickets):
        if i[0] == 'ICN':
            dfs(i[1], tickets[:s]+tickets[s+1:], ['ICN'])
    answer.sort()
    return answer[0]

if __name__ == '__main__':
    solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])