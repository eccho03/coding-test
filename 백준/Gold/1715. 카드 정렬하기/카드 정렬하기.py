import heapq

N = int(input())
numbers = [int(input()) for _ in range(N)]
heap = []

for i in range(N):
    heapq.heappush(heap, numbers[i])

# print(heap)

answer = 0
while len(heap)>1:
    cur1 = heapq.heappop(heap)
    cur2 = heapq.heappop(heap)
    cost = cur1 + cur2
    answer += cost

    heapq.heappush(heap, cost)

print(answer)