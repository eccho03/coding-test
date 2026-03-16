def snake(arr):

    # 우 하 좌 상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    ti,tj,dr = 0, 0, 0

    for i in range(N*N):
        arr[ti][tj] = i+1
        ti,tj = ti+di[dr], tj+dj[dr]

        if ti<0 or ti>=N or tj<0 or tj>=N or arr[ti][tj]!=0:
            ti, tj = ti - di[dr], tj - dj[dr]
            dr = (dr+1)%4
            ti, tj = ti + di[dr], tj + dj[dr]

    return arr

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    arr=[[0]*N for _ in range(N)]
    narr = [x[:] for x in arr]
    arr = snake(narr)
    print("#%d" % test_case)
    for i in range(N):
        print(*arr[i])
    # ///////////////////////////////////////////////////////////////////////////////////