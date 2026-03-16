T = int(input())
for _ in range(T):
    N = int(input())
    note1 = list(map(int, input().split()))

    M = int(input())
    note2 = list(map(int, input().split()))

    note1.sort()

    #print(note1,note2)

    for num in note2:
        start, end = 0, N-1
        mid = -1

        while start<=end:
            mid=(start+end)//2
            if note1[mid]==num:
                break
            elif num<note1[mid]:
                end = mid-1
            else:
                start = mid+1


        #print(mid)

        if note1[mid]==num:
            print(1)
        else:
            print(0)