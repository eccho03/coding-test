N, L = map(int, input().split())
locations = list(map(int, input().split()))
locations.sort()

idx=0
cnt=0

for loc in locations:

    if idx>=loc: #이미 그 전 좌표로 인해 커버하고 있음
        continue

    cnt+=1
    idx = loc-0.5+L

print(cnt)