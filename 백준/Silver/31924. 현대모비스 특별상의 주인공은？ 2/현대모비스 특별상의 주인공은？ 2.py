txt = "MOBIS"
def count_mobis():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == txt[0]:
                for di, dj in ((-1,0),(1,0),(0,-1),(0,1),(-1,1),(1,-1),(-1,-1),(1,1)):
                    ni, nj = i, j
                    is_mobis = True
                    for ch in txt[1:]:
                        ni += di
                        nj += dj
                        if 0<=ni<N and 0 <=nj<N and arr[ni][nj] == ch:
                            continue
                        else:
                            is_mobis = False
                            break
                    if is_mobis:
                        cnt += 1
    return cnt


N = int(input())
arr = [input() for _ in range(N)]
print(count_mobis())