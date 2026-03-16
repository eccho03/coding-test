N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)

def find_target(ti, tj, v):
    lst = []
    v[ti][tj]=1
    lst.append((ti, tj))

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = ti+di, tj+dj

        if 0<=ni<N and 0<=nj<N and v[ni][nj]==0:
            v[ni][nj]=1
            lst.append((ni, nj))

    return lst

def cal_cost(lst):
    flower_cost = 0

    for ci, cj in lst:
        flower_cost += arr[ci][cj]

    return flower_cost

def clear_flower(lst):
    for ci, cj in lst:
        v[ci][cj]=0

def dfs(cur_cost, cnt):
    global cost
    if cnt == 3:
        # print(cur_cost)
        cost = min(cost, cur_cost)
        return cost

    for i in range(N):
        for j in range(N):
            if v[i][j]==0:
                lst = find_target(i, j, v)
                if len(lst)==5:
                    dfs(cur_cost + cal_cost(lst), cnt+1)
                clear_flower(lst)

    return cost


v = [[0]*N for _ in range(N)]
cost = float('inf')

ans = dfs(0, 0)
print(ans)