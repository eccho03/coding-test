from itertools import combinations

def find_dis(a, b):
    dis = 0
    for i, j in zip(a, b):
        if i!=j:
            dis+=1
    return dis

T = int(input())
for _ in range(T):
    N = int(input())
    mbti = list(input().split())
    mn_dist = float('inf')
    
    
    if N>32:
        print(0)
        continue

    for case in combinations(mbti, 3):
        dist = 0
        cur_dist = find_dis(case[0], case[1])+find_dis(case[1], case[2]) + find_dis(case[2], case[0])
        #print(dist)
        mn_dist = min(mn_dist, cur_dist)

    print(mn_dist)