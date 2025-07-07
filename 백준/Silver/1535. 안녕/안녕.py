from itertools import combinations

N = int(input())
lose = list(map(int, input().split()))
joy = list(map(int, input().split()))

d = [0]*101
for i in range(N):
    for j in range(100, lose[i], -1):
        d[j]=max(d[j], d[j-lose[i]]+joy[i])

print(max(d))
