import sys
sys.setrecursionlimit(10**9)

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

n, m = map(int, sys.stdin.readline().split())

parent = [0] * (n + 1)
result = []

for i in range(1, n + 1):
    parent[i] = i

for _ in range(m):
    fun, a, b = map(int, sys.stdin.readline().split())
    if fun == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            result.append("YES")
        else:
            result.append("NO")

for r in result:
    print(r)