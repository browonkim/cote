def solution(s: str):
    # split, capitalize, title 다 못 씀 : 쓸 경우 테스트케이스 오류남
    return ''.join([s[0].upper()] + [y.upper() if x == " " else y.lower() for x, y in zip(s, s[1:])])


if __name__ == "__main__":
    print(solution("  a"))
