def solution(park, routes):
    answer = []
    new_park = []
    N, M = len(park), len(park[0])
    
    for i in range(N):
        new_park.append(list(park[i]))
    
    # print(new_park)
    
    directions = {'N': (-1,0), 'S': (1,0), 'W': (0,-1), 'E': (0, 1)}
    
    def find_si_sj():
        for i in range(N):
            for j in range(M):
                if new_park[i][j]=='S':
                    return i, j
    
    ci, cj = find_si_sj() #현재위치
    
    for route in routes:
        dir, cnt = route.split(" ")
        di, dj = directions[dir]
        # print(di, dj)
        
        flag = True
        ni, nj = ci, cj
        for i in range(int(cnt)):
            ni+=di
            nj+=dj

            if not(0<=ni<N and 0<=nj<M and new_park[ni][nj]!='X'):
                flag = False
                break
        if flag:
            ci, cj = ni, nj
        
        # print(ci, cj)
    
    
    return [ci, cj]