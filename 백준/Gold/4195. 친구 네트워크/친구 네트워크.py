import sys

def find(x):
    if parent[x]!=x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a==b:
        return size[a]

    if a<b:
        parent[b]=a
        size[a]+=size[b]
    else:
        parent[a]=b
        size[b]+=size[a]
    return size[find(a)]

T = int(input())
for _ in range(T):
    N = int(sys.stdin.readline())
    ans = []
    nicknames = {}
    V = 0
    parent = []
    size = []

    for _ in range(N):
        fri1, fri2 = sys.stdin.readline().split()

        if fri1 not in nicknames:
            nicknames[fri1]=V
            parent.append(V)
            size.append(1)
            V+=1
        if fri2 not in nicknames:
            nicknames[fri2]=V
            parent.append(V)
            size.append(1)
            V+=1


        a = nicknames[fri1]
        b = nicknames[fri2]
        result = str(union(a,b))
        sys.stdout.write(result+"\n")
    # print('\n'.join(ans))