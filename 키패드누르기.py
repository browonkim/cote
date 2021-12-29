def solution(numbers, hand):
    answer = ''
    left = {1: (0, 0), 4: (1, 0), 7: (2, 0), '*': (3, 0)}
    right = {3: (0, 2), 6: (1, 2), 9: (2, 2), '#': (3, 2)}
    center = {2: (0, 1), 5: (1, 1), 8: (2, 1), 0: (3, 1)}
    left_thumb = (3, 0)
    right_thumb = (3, 2)
    for i in numbers:
        if i in left:
            answer += 'L'
            left_thumb = left[i]
        elif i in right:
            answer += 'R'
            right_thumb = right[i]
        else:
            cur = center[i]
            l = abs(left_thumb[0] - cur[0]) + abs(left_thumb[1] - cur[1])
            r = abs(right_thumb[0] - cur[0]) + abs(right_thumb[1] - cur[1])
            if l < r:
                answer += 'L'
                left_thumb = cur
            elif l > r:
                answer += 'R'
                right_thumb = cur
            else:
                if hand == "left":
                    answer += 'L'
                    left_thumb = cur
                else:
                    answer += 'R'
                    right_thumb = cur
    return answer

if __name__ == "__main__":
    print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))