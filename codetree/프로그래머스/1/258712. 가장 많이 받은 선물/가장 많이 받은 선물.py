from itertools import combinations
from collections import defaultdict

def solution(friends, gifts):
    
    N = len(friends)
    answer = [0]*(N+1)
    
    gift_cnt = [0]*(N+1)
    graph = [[0]*(N+1) for _ in range(N+1)]
    name_list = dict()
    num = 1
    
    for i in range(N):
        name_list[friends[i]] = num
        num+=1
    
    # print(name_list)
        
    for i in range(len(gifts)):
        giver, taker = gifts[i].split(" ")
        gift_cnt[name_list[giver]]+=1
        gift_cnt[name_list[taker]]-=1
        graph[name_list[giver]][name_list[taker]]+=1
    
    # print(graph)
    # print(gift_cnt)
    
    
    for i in combinations(friends, 2):
        A, B = i
        if graph[name_list[A]][name_list[B]] > graph[name_list[B]][name_list[A]]:
            answer[name_list[A]]+=1
        elif graph[name_list[A]][name_list[B]] == graph[name_list[B]][name_list[A]]:
            if gift_cnt[name_list[A]]>gift_cnt[name_list[B]]:
                answer[name_list[A]]+=1
            elif gift_cnt[name_list[A]]<gift_cnt[name_list[B]]:
                answer[name_list[B]]+=1
        else:
            answer[name_list[B]]+=1
    
    return max(answer)