T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))
    orders = []

    q = []
    for i in range(N):
        q.append((i+1, priorities[i]))

    while q:
        cur, cur_prior = q.pop(0)
        flag=0

        for i in range(len(q)):
            if q[i][1]>cur_prior:
                q.append((cur, cur_prior))
                flag=1
                break
        if flag==0:
            orders.append(cur)

    # print(orders)
    for i in range(N):
        if orders[i]==M+1:
            print(i+1)
            break