def solution(bridge_length, weight, truck_weights: list):
    if bridge_length == 1:
        return len(truck_weights)
    # if bridge_length >= 2
    bridge = [0] * bridge_length
    total = bridge[0]
    time = 1
    while len(truck_weights) != 0:
        time += 1
        total -= bridge.pop(0)
        if total+truck_weights[0] <= weight:
            bridge.append(truck_weights.pop(0))
            total += bridge[-1]
        else:
            bridge.append(0)

    for i in range(len(bridge)-1, -1, -1):
        if bridge[i] > 0:
            time += i
            break
    return time

if __name__ == "__main__":
    print(solution(	100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))