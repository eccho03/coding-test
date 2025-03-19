def move(arr):
    # 행 단위로 이동(같은 값 합치기)

    for i in range(len(arr)):
        num = 0
        tlst = []
        for n in arr[i]:
            #해당 행에서 숫자 하나씩 처리
            if n == 0: # 빈칸은 처리 안 함
                continue
            if n == num: # 기준 숫자와 같은 경우 -> 합침
                tlst.append(n*2)
                num = 0
            else:  # 기준 숫자와 다른 경우
                if num != 0:
                    tlst.append(num)
                num = n

        # 종료 후 기준 숫자 있으면 tlst 추가 그리고 남은자리 0으로 채움
        if num != 0:
            tlst.append(num)

        arr[i] = tlst+[0]*(N - len(tlst))

def dfs(n, arr):
    global ans

    if n == 5:
        ans = max(ans, max(map(max, arr)))
        return

    # 좌측 이동 기준
    narr = [lst[:] for lst in arr] # 딥카피 해서 전달
    move(narr)
    dfs(n + 1, narr)

    # 우측
    narr = [lst[::-1] for lst in arr]  # array를 반대방향으로 딥카피 해서 전달
    move(narr)
    dfs(n + 1, narr)

    # 상
    arr_t = list(map(list, zip(*arr))) # 열 -> 행으로
    narr = [lst[:] for lst in arr_t]
    move(narr)
    dfs(n + 1, narr)

    # 하
    narr = [lst[::-1] for lst in arr_t]
    move(narr)
    dfs(n + 1, narr)


N = int(input())
ans = 0
board = [list(map(int, input().split())) for _ in range(N)]

dfs(0, board)
print(ans)