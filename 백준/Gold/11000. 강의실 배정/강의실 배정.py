import heapq

N = int(input())
classes = [list(map(int, input().split())) for _ in range(N)]
classes.sort(key=lambda x: x[0]) # 시작 시간 기준 정렬

# print(heap)

rooms = []
heapq.heappush(rooms, classes[0][1])

for i in range(1, N):
    cur_start, cur_end = classes[i][0], classes[i][1]

    # 방 재사용
    if rooms[0] <= cur_start:
        heapq.heappop(rooms)
        heapq.heappush(rooms, cur_end)
    else: # 새로운 강의실 필요
        heapq.heappush(rooms, cur_end)
    # print(cur_class, nxt_class)
    # print(rooms)

print(len(rooms))
