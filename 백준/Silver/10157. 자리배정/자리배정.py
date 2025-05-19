def myprint(arr):
    for i in range(R):
        print(*arr[i])
    print()

C, R = map(int, input().split())
K = int(input())

if K > R*C:
    print(0)
else:
    cnt = 1
    num = [[0]*C for _ in range(R)]

    si, sj = R-1, 0

    directions = [(-1,0),(0,1),(1,0),(0,-1)] # 상우하좌(시계)
    dir = 0

    ni,nj = 0,0

    while cnt!=R*C:
        di, dj = directions[dir]
        num[si][sj] = cnt
        cnt += 1

        ni,nj = si+di, sj+dj

        if ni<0 or ni>=R or nj<0 or nj>=C or num[ni][nj]!=0:
            dir = (dir+1)%4
            cnt-=1

            continue
        si,sj = ni,nj

    num[ni][nj] = R*C
    #myprint(num)


    for i in range(R):
        for j in range(C):
            if num[i][j]==K:
                print(j+1, R-i)