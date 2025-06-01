T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    arr1.sort()
    arr2.sort()

    # print(arr1)
    # print(arr2)

    ans = 0

    for i in range(N):
        start, end = 0, M-1

        while start <= end:
            mid = (start+end)//2
            #print(f'{arr1[i]} - {arr2[mid]}')
            if arr1[i] > arr2[mid]:
                start = mid+1
            else:
                end = mid-1
            # else:
            #     break
        #print(f'{arr1[i]}: {ans}')
        ans+=start

    print(ans)