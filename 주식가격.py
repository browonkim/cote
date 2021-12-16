def solution(prices):
    l = len(prices)
    result, stack = [0] * l, []
    for seq, price in enumerate(prices):
        if len(stack) == 0:
            stack.insert(0, (price, seq))
        else:
            while len(stack) > 0 and stack[0][0] > price:
                top = stack.pop(0)
                result[top[1]] = seq - top[1]
            stack.insert(0, (price, seq))
    for p, s in stack:
        result[s] = l - s - 1
    return result

if __name__ =="__main__":
    print(solution([5,4,3,2,1]))