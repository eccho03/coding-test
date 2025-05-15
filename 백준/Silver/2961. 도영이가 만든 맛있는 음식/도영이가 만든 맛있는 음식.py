def dfs(idx, cur_s, cur_b, used):
    global mn_taste

    if idx == N:
        return

    s, b = taste[idx]
    cur_s *= s
    cur_b += b
    tmp_taste = abs(cur_s - cur_b)
    if tmp_taste < mn_taste:
        #print(cur_s, cur_b)
        mn_taste = tmp_taste

    dfs(idx+1, cur_s, cur_b, True)
    dfs(idx+1, cur_s//s, cur_b-b, used)


mn_taste = float('inf')
N = int(input())
taste = [list(map(int, input().split())) for _ in range(N)]
dfs(0, 1, 0, False)

print(abs(mn_taste))