from itertools import combinations

S = input()
N = len(S)
ans = []

arr = [i for i in range(1,N)]

for i in combinations(arr, 2):
    ll, rr = i
    left, mid, right = S[:ll], S[ll:rr], S[rr:]
    re_left, re_mid, re_right = left[::-1], mid[::-1], right[::-1]
    tmp = re_left + re_mid + re_right
    #print(tmp)
    ans.append(tmp)

ans.sort()
print(ans[0])