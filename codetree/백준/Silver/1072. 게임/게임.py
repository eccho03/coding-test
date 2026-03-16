def get_win_rate(x, y):
    return (y * 100) // x

X,Y = map(int,input().split())
Z = get_win_rate(X,Y)

ans = 0

left, right = 1, 1_000_000_000

if Z>=99:
    print(-1)
else:
    ans-=1
    while left <= right:
        mid = (left+right)//2
        if get_win_rate(X+mid,Y+mid)>Z:
            ans = mid
            right=mid-1
        else:
            left=mid+1

    print(ans)