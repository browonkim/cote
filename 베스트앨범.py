from heapq import *
def solution(genres, plays):
    class Music:
        def __init__(self, first_plays, first_index):
            self.list = []
            heappush(self.list, (-first_plays, first_index))
            self.size = first_plays

        def add_music(self,  music_plays, music_index):
            heappush(self.list, (-music_plays, music_index))
            self.size += music_plays

        def get_size(self):
            return self.size

        def get_unit(self):
            return heappop(self.list)

        def is_empty(self):
            return True if len(self.list) == 0 else False

    answer = []
    genres_chart = {}
    for i in range(len(plays)):
        if genres[i] in genres_chart:
            genres_chart[genres[i]].add_music(plays[i], i)
        else:
            genres_chart[genres[i]] = Music(plays[i], i)
    k = sorted(list(genres_chart.keys()), key=lambda a: genres_chart[a].get_size(), reverse=True)
    for t in k:
        answer.append(genres_chart[t].get_unit()[1])
        if not genres_chart[t].is_empty():
            answer.append(genres_chart[t].get_unit()[1])
    return answer


if __name__ == "__main__":
    print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))

