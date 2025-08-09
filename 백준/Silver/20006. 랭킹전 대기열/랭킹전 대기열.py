def is_room(cur_lv):
    for i in range(len(rooms)):
        cur_room = rooms[i]
        # print(cur_room)
        if len(cur_room)<=0:
            continue

        target_lv = cur_room[0][0]
        if target_lv-10<=cur_lv<=target_lv+10 and len(cur_room)<M:
            return i

    return -1

N, M = map(int, input().split())
players = [list(input().split()) for _ in range(N)]
rooms = [[] for _ in range(N+1)]
room_idx = 0
for lv, name in players:
    lv = int(lv)
    # 입력된 순서대로 게임 시작
    idx = is_room(lv)
    # print(idx)
    if idx==-1: # 입장 가능한 방이 없음
        rooms[room_idx].append([lv, name])
        room_idx+=1
    else:
        rooms[idx].append((lv, name))


for room in rooms:
    if len(room)<=0:
        break

    if len(room)==M:
        print("Started!")
    else:
        print("Waiting!")
    for (cur_lv, cur_player) in sorted(room, key=lambda x: x[1]):
        print(cur_lv, cur_player)