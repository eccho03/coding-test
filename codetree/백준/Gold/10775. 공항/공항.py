def find(x):
    if parent[x]!=x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

G = int(input())
P = int(input())

parent = [0]*(G+1)
for i in range(1,G+1):
    parent[i]=i

ans=0
for i in range(P):
    gi = int(input())
    root = find(gi)
    #print(parent)
    if root==0:
        break
    union(root,root-1)
    ans+=1

print(ans)