n = int(input())
house = []
d = [[0, 0, 0] for _ in range(n)]
for i in range(n):
    r, g, b = map(int, input().rstrip().split())
    house.append([r, g, b])

d[0] = house[0]

for i in range(1, n):
    d[i][0] = house[i][0] + min(d[i-1][1], d[i-1][2])
    d[i][1] = house[i][1] + min(d[i-1][0], d[i-1][2])
    d[i][2]= house[i][2] + min(d[i-1][0], d[i-1][1])

ans = min(d[i][0], d[i][1], d[i][2])
print(ans)