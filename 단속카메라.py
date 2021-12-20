def solution(routes: list):
    cars = len(routes)
    routes.sort()
    count = 0
    cameras = 0

    # 첫번째 car 의 범위 (left, right)를 기준으로
    # 두번째 car 의 범위와 겹치는 부분을 구한다.
    # 만약에 두번째와 겹치는 부분이 없다면 그냥 count 를 하나 증가시키고 다음으로 넘어간다
    # 그렇게 겹치는 부분을 구한다 계속해서
    left, right = routes[0][0], routes[0][1]
    for i in routes:
        i_left, i_right = i[0], i[1]
        if i_left > right:
            count += 1
            left = i_left
            right = i_right
        else:
            left = i_left
            right = right if right < i_right else i_right
    return count + 1


if __name__ == "__main__":
    print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
