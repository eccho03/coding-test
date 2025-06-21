N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)

from collections import deque
def find_target(ti, tj, v):
    lst = []
    v[ti][tj]=1
    lst.append((ti, tj))

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = ti+di, tj+dj

        if is_valid(ni, nj):
            v[ni][nj]=1
            lst.append((ni, nj))

    return lst

def is_valid(ti, tj):
    if 0<=ti<N and 0<=tj<N and v[ti][tj]==0:
        return True
    return False

def cal_cost(lst):
    n = len(lst)
    flower_cost = 0

    for i in range(n):
        ci, cj = lst[i]
        flower_cost += arr[ci][cj]

    return flower_cost

def clear_flower(lst):
    n = len(lst)

    for i in range(n):
        ci, cj = lst[i]
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