N,M,K = map(int,input().split())
fireball = []
for i in range(M):
    r,c,m,s,d = map(int,input().split())
    fireball.append([r-1,c-1,m,s,d])

arr = [[0]*N for _ in range(N)]
#               0         1      2       3       4       5       6       7
directions = ((-1, 0),(-1, 1),(0 , 1),(1 , 1),(1 , 0),(1, -1),(0, -1),(-1,-1))


for turn in range(K):
    arr = [[[] for _ in range(N)] for _ in range(N)]

    for idx in range(len(fireball)):
        ci,cj,m,s,d = fireball[idx]

        # 1. 모든 파이어볼 d 방향 s만큼 이동
        di,dj = directions[d]
        ni,nj = (ci+di*s)%N, (cj+dj*s)%N
        fireball[idx] = [ni,nj,m,s,d]
        arr[ni][nj].append([m,s,d])
    #print(fireball)

    # 2. 이동이 모두 끝나고 2개 이상인 경우
    fireball.clear()
    for i in range(N):
        for j in range(N):
            if len(arr[i][j])==0:   continue
            elif len(arr[i][j])==1:
                m,s,d = arr[i][j][0]
                fireball.append([i,j,m,s,d])
            else:
                total_m = sum(m for m,s,d in arr[i][j])
                total_s = sum(s for m,s,d in arr[i][j])
                total_cnt = len(arr[i][j])

                new_m = total_m//5
                new_s = total_s//total_cnt

                if new_m==0:    # 질량 0이면 사라짐
                    continue

                is_even = all(d%2==0 for m,s,d in arr[i][j])
                is_odd = all(d%2==1 for m,s,d in arr[i][j])

                if is_even or is_odd:
                    new_d = [0,2,4,6]
                else:
                    new_d = [1,3,5,7]

                for nd in new_d:
                    fireball.append([i,j,new_m,new_s,nd])

    #print(fireball)

answer = sum(m for i,j,m,d,s in fireball)
print(answer)