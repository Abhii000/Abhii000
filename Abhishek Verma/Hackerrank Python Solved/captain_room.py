x = int(input())
rooms = [int(a) for a in input().split()]
counts = {}

for room in rooms:
    counts[room] = counts.get(room, 0) + 1

for room, count in counts.items():
    if count == 1:
        print(room)
        break
