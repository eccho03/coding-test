def check_target(target, ll):
    if target[0][0] == target[0][ll-1] == target[ll-1][0] == target[ll-1][ll-1]:
        return True
    return False

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
# print(arr)
mx_ll = 0

for ll in range(1, min(N,M)+1):
    for i in range(N-ll+1):
        for j in range(M-ll+1):
            target=[]
            for si in range(ll):
                tmp = []
                for sj in range(ll):
                    # print(arr[si+i][sj+j], end=' ')
                    tmp.append(arr[si+i][sj+j])
                target.append(tmp)
            #     print()
            # print(target)
            if check_target(target, ll):
                mx_ll = ll

    #         print()
    # print()

print(mx_ll**2)