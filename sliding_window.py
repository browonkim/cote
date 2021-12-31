def sliding_window(arr, k):
    win_sum = 0
    max_sum = 0
    start = 0
    for end in range(len(arr)):
        win_sum += arr[end]
        if end >= k-1:
            max_sum = max(max_sum, win_sum)
            win_sum -= arr[start]
            start += 1
    return max_sum

