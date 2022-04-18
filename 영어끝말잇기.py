def solution(n, words):
    s = set()
    s.add(words[0])
    for seq, word in enumerate(words[1:]):
        if words[seq][-1] != word[0] or word in s:
            return [(seq+2)%n, (seq+1)//n+1]
        s.add(word)
        print(s)
    else:
        return [0, 0]

if __name__ == "__main__":
    print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))