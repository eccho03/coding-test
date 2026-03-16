def solution(n, results):
    def dfs1(start):
        v[start] = True
        cnt[start]+=1
        print(start, end=' ')
        for i in win[start]:
            if v[i]==0:
                dfs1(i)

    def dfs2(start):
        v[start] = True
        cnt[start]+=1
        print(start, end=' ')
        for i in lose[start]:
            if v[i]==0:
                dfs2(i)

    answer = 0
    win = [[] * (n+1) for _ in range(n+1)]
    lose = [[] * (n+1) for _ in range(n+1)]
    
    cnt = [0] * (n+1)
    
    for i,j in results:
        win[j].append(i)
    
    for i,j in results:
        lose[i].append(j)
        
    for i in range(1, n+1):
        v = [0] * (n+1)
        dfs1(i)
        print()
    print("-----")
    for i in range(1, n+1):
        v = [0] * (n+1)
        dfs2(i)
        print()
    print(cnt)
    
    answer = cnt.count(n+1)
    return answer