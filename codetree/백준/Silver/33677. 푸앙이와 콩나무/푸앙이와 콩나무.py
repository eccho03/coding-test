import heapq
def bfs(start):
    pq = []
    v = dict()

    # day / water / node
    heapq.heappush(pq, (0, 0, start))
    v[start] = (0,0)

    while pq:
        day, water, cur = heapq.heappop(pq)
        if cur == N:
            return day, water

        for nxt, w in [(cur+1,1), (cur*3,3), (cur**2,5)]:
            if nxt>N:
                continue

            nxt_day = day + 1
            nxt_water = water + w

            if (nxt not in v or
                    v[nxt][0] > nxt_day or
                    (v[nxt][0] == nxt_day and v[nxt][1] > nxt_water)):
                v[nxt] = (nxt_day, nxt_water)
                heapq.heappush(pq, (nxt_day, nxt_water, nxt))

    return -1



N = int(input())

days, water = bfs(0)
print(days, water)