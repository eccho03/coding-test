while True:
    try:
        n = int(input())

        cur = "1"
        while True:
            # n의 배수
            if int(cur)%n==0:
                num = str(cur)

                flag = True
                for i in range(len(num)):
                    if num[i]!='1':
                        flag = False
                        break

                if flag:
                    print(len(num))
                    break

            cur+="1"
    except EOFError:
        break