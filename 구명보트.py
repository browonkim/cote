def solution(people: list, limit: int):
    people.sort()
    left, right, total = 0, len(people)-1, 0
    non_visited = []
    while left < right:
        while left < right:
            if people[right] + people[left] <= limit:
                break
            non_visited.append(people[right])
            right -= 1
        else:
            if left == right:
                total += 1
            break
        total += 1
        left += 1
        right -= 1
        if left >= right:
            if left == right:
                total += 1
                break
    return total + len(non_visited)


if __name__ == "__main__":
    print(solution([10, 30, 50, 70, 80, 88, 70, 90], 100))
