def binary(target):
    start, end = 0, M-1

    while start <= end:
        mid = (start + end) // 2

        #print("mid:",mid)

        if target > woman[mid]:
            start = mid + 1
        elif target < woman[mid]:
            end = mid - 1
        else:
            return mid
    return -1


while True:
    N, M = map(int, input().split())

    if (N,M)==(0,0):
        break

    man = [int(input()) for _ in range(N)]
    woman = [int(input()) for _ in range(M)]

    cnt = 0

    for i in range(N):
        if binary(man[i]) != -1:
            cnt += 1

    print(cnt)