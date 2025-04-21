X, Y, W, S = map(int, input().split())
ci,cj = 0,0
ans1 = (X+Y)*W
ans2 = min(X, Y)*S + abs(X-Y)*W
ans3 = 0
if (X+Y)%2==0:
    ans3 = max(X, Y)*S
else:
    ans3 = (max(X, Y)-1)*S+W
print(min(ans1, ans2, ans3))
