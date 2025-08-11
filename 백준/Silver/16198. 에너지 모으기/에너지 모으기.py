def dfs(w_lst, energy):
    global mx_energy

    if len(w_lst)==2:
        mx_energy = max(mx_energy, energy)
        return

    for i in range(1, len(w_lst)-1):
        new_energy = w_lst[i-1]*w_lst[i+1]
        x = w_lst.pop(i)
        dfs(w_lst, energy+new_energy)
        w_lst.insert(i, x)

N = int(input())
W = list(map(int, input().split()))
mx_energy = 0
v = [0]*N # 구슬 선택 여부
dfs(W, 0)
print(mx_energy)