while True:
    try:
        X = int(input())
        N = int(input())
        lego = [int(input()) for _ in range(N)]
        lego.sort()

        start, end = 0, N-1
        flag = 0
        while start<end:
            tmp = lego[start]+lego[end]

            # print(tmp/(10**7))
            if tmp>X*(10**7):
                end-=1
            elif tmp<X*(10**7):
                start+=1
            else:
                # print(lego[start] , lego[end])
                flag = 1
                break

        if flag:
            print("yes", lego[start], lego[end])
        else:
            print("danger")
    except:
        break