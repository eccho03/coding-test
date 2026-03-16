import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

parent = [0] * (n + 1)
edges = []
result = 0

# 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        # 싸이클 x
        union_parent(parent, a, b)
        result += cost

print(result)