from itertools import permutations

def find_cost(lst):
    cost = 0
    # lst = [0,1,2,3,0]
    for i in range(len(lst)-1):
        if arr[lst[i]][lst[i+1]]==0:
            return -1
        cost+=arr[lst[i]][lst[i+1]]

    return cost

N = int(input())
v = [0]*N
arr = [list(map(int, input().split())) for _ in range(N)]
num = [i for i in range(N)]
mn_cost = float('inf')

for i in permutations(num, N):
    order = list(i)+[list(i)[0]]

    cost = find_cost(order)

    if cost<mn_cost and cost!=-1:
        mn_cost = cost

    # print(order)
    # print(cost)
print(mn_cost)