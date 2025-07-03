N = int(input())
house = list(map(int, input().split()))
house.sort()
# print(house)
ans = 0

if N==1:
    ans = house[0]
else:
    # 짝수면
    if len(house)%2==0:
        idx = len(house) // 2
        ans = house[idx-1]

    else:
        idx = (len(house)-1) // 2
        ans = house[idx]

print(ans)