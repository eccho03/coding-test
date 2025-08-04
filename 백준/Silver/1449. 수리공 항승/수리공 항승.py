N, L = map(int, input().split())
locations = list(map(int, input().split()))
locations.sort()

ans = 0 # 테이프 개수
cur_loc = locations[0]
for i in range(1,N):
    if cur_loc+L > locations[i]:
        pass
    else:
        ans+=1
        cur_loc = locations[i]

print(ans+1)