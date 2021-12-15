from itertools import combinations

def solution(cards):
    ideal_maximum = len(cards)//3
    possible_set = set()
    for card in combinations(cards, 3):
        num = len({card[0][0], card[1][0], card[2][0]})
        color = len({card[0][1], card[1][1], card[2][1]})
        shape = len({card[0][2], card[1][2], card[2][2]})
        shadow = len({card[0][3], card[1][3], card[2][3]})
        if num == 1 or num == 3:
            if color == 1 or color == 3:
                if shape == 1 or shape == 3:
                    if shadow == 1 or shadow == 3:
                        possible_set.add(card)

    def dfs(left, n):
        if len(left) < 3:
            return n
        temp_max = n
        for i in combinations(left, 3):
            if i in possible_set:
                temp = dfs([x for x in left if x not in i], n+1)
                if temp == ideal_maximum:
                    return temp
                temp_max = temp if temp > temp_max else temp_max
        return temp_max

    return dfs(cards, 0)


if __name__ == "__main__":
    print(solution(["1PEW", "1REW", "1GEW", "2PEW", "2RTS", "2GDF", "1GDF","1GDW","1GDS"]))
    print(solution(["1PEW", "1REW", "1GEW", "2PEW", "2RTS", "2GDF", "3GDF"]))
