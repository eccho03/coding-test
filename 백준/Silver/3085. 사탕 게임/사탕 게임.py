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
    mx = 1
    for i in range(N):
        row_cnt = col_cnt = 1
        for j in range(1, N):
            if arr[i][j] == arr[i][j-1]:
                row_cnt += 1
            else:
                row_cnt = 1
            if arr[j][i] == arr[j-1][i]:
                col_cnt += 1
            else:
                col_cnt = 1
            mx = max(mx, row_cnt, col_cnt)
    return mx

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
