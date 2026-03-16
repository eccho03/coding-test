from collections import deque

def give_water(giver, taker, mx_taker):
    while True:
        giver-=1
        taker+=1

        if giver<=0 or taker>=mx_taker:
            break

    return giver, taker

def bfs(sa, sb, sc):
    q = deque()
    v = set()

    q.append((sa, sb, sc))
    v.add((sa, sb, sc))

    while q:
        ca, cb, cc = q.popleft()

        # print(ca, cb, cc)
        if ca==0:
            ans.append(cc)

        idx=0
        # a->b / a->c / b->c / b->a / c->a / c->b
        for way in (give_water(ca, cb, B), give_water(ca, cc, C),
                    give_water(cb, cc, C),give_water(cb, ca, A),
                    give_water(cc, ca, A),give_water(cc, cb, B)):
            if idx==0:
                na, nb, nc = way[0], way[1], cc
            elif idx==1:
                na, nb, nc = way[0], cb, way[1]

            elif idx==2:
                na, nb, nc = ca, way[0], way[1]
            elif idx==3:
                na, nb, nc = way[1], way[0], cc

            elif idx==4:
                na, nb, nc = way[1], cb, way[0]
            else:
                na, nb, nc = ca, way[1], way[0]

            if (na, nb, nc) not in v and 0<=na<=A and 0<=nb<=B and 0<=nc<=C:
                q.append((na, nb, nc))
                v.add((na, nb, nc))

            idx+=1


A, B, C = map(int, input().split())
sa, sb, sc = 0, 0, C
ans = []
bfs(sa, sb, sc)
ans.sort()
print(*ans)