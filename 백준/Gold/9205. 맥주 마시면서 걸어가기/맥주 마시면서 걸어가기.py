from collections import deque


def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def bfs():
    queue = deque([start])
    visited.add(start)

    while queue:
        x, y = queue.popleft()

        if distance(x, y, end[0], end[1]) <= 1000:
            return "happy"

        for nx, ny in graph:

            if (nx, ny) not in visited and distance(x, y, nx, ny) <= 1000:
                visited.add((nx, ny))
                queue.append((nx, ny))

    return "sad"


T = int(input())
for _ in range(T):
    # 맥주 판매 편의점 개수
    n = int(input())
    graph = []

    start = tuple(map(int, input().split()))

    for _ in range(n):
        graph.append(tuple(map(int, input().split())))

    end = tuple(map(int, input().split()))

    visited = set()

    print(bfs())
