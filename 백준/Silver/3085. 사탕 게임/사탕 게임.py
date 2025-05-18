N = int(input())
arr = [list(input()) for _ in range(N)]

def check_diff():
    target = []

    for i in range(N):
        for j in range(N):

            for di,dj in ((1,0),(0,1)):
                ni,nj = i+di,j+dj

                if ni<N and nj<N:
                    target.append((i,j,ni,nj))

    return target

def find_same(arr):
    mx_cnt = 0
    for i in range(N):

        for j in range(N):
            # 연속 부분 - 행 카운트
            ni,nj = i,j
            row_cnt, col_cnt = 0,0

            while True:
                nj+=1
                row_cnt+=1
                if nj>=N or arr[i][j]!=arr[i][nj]:
                    break

            ni,nj = i,j
            while True:
                ni+=1
                col_cnt+=1
                if ni >= N or arr[i][j] != arr[ni][j]:
                    break
            #print(f'{i}, {j}: {row_cnt, col_cnt}')
            mx_cnt = max(mx_cnt, max(row_cnt,col_cnt))

    return mx_cnt

def myarr(arr):
    for i in range(N):
        print(*arr[i])
    print()


# 사탕의 색이 다른 인접한 두 칸 고르기
target = check_diff()
#print(target)
mx_ans = 0

for si,sj,ei,ej in target:
    narr = [x[:] for x in arr]
    tmp = narr[si][sj]
    narr[si][sj] = narr[ei][ej]
    narr[ei][ej] = tmp

    #print(f'({si}, {sj})({ei}, {ej}) 교환')
    #myarr(narr)
    ans = find_same(narr)
    mx_ans = max(mx_ans, ans)
    # print(narr)
    # print()
print(mx_ans)
