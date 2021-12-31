def solution(k, room_number):
    rooms = {}
    result = []

    def find(r):
        if r not in rooms:
            rooms[r] = r + 1
            return r
        else:
            empty_room = find(rooms[r])
            rooms[r] = empty_room + 1
            return empty_room

    for i in room_number:
        result.append(find(i))

    return result


if __name__ == "__main__":
    print(solution(10, [1, 3, 4, 1, 3, 1]))
