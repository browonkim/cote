def solution(n, m, points, hands):
    chain = {"S": 0, "R": 1, "P": 2}
    reverse_chain = {0: "S", 1: "R", 2: "P"}
    score = [0] * n

    def get_score(first, second, cur_point):
        nonlocal score
        if abs(chain[first] - chain[second]) == 1:
            winner = reverse_chain[max(chain[first], chain[second])]
            loser = reverse_chain[min(chain[first], chain[second])]
        else:
            loser = reverse_chain[max(chain[first], chain[second])]
            winner = reverse_chain[min(chain[first], chain[second])]
        if cur_point < 0:
            for x in temp_dict[loser]:
                score[x] += cur_point
        else:
            for x in temp_dict[winner]:
                score[x] += cur_point

    for i in range(m):
        temp_dict = {"S": [], "R": [], "P": []}
        temp_set = set()
        for seq, j in enumerate(hands[i]):
            temp_dict[j] += [seq]
            temp_set.add(j)
        if len(temp_set) == 1:
            if i != m - 1:
                points[i + 1] += points[i]
        elif len(temp_set) == 2:
            t = list(temp_set)
            get_score(t[0], t[1], points[i])
        else:
            count = {}
            for length, key in [(len(temp_dict["S"]), "S"), (len(temp_dict["R"]), "R"), (len(temp_dict["P"]), "P")]:
                if length not in count:
                    count[length] = [key]
                else:
                    count[length] += [key]
            if len(count.keys()) == 1:
                if i != m - 1:
                    points[i + 1] += points[i]
            elif len(count.keys()) == 2:
                winner = ""
                for key in count.keys():
                    if len(count[key]) == 1:
                        winner = count[key][0]
                        break
                for x in temp_dict[winner]:
                    score[x] += points[i]
            else:
                if points[i] < 0:
                    minimum = min(count.keys())
                    count.pop(minimum)
                    a = list(count.values())
                    get_score(a[0][0], a[1][0], points[i])
                else:
                    maximum = max(count.keys())
                    count.pop(maximum)
                    a = list(count.values())
                    get_score(a[0][0], a[1][0], points[i])

    return max(score)

if __name__ == "__main__":
    print(solution(6, 5, [5, -2, 1, 3, -5], ["PSPRSS", "SSRRSS", "RRRRRR", "RRSSPP", "SSSRRP"]))