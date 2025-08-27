from collections import Counter

N, M = map(int, input().split())
dnas = [input().rstrip() for _ in range(N)]
mn_dna=""
for i in range(M):
    target=[]
    for j in range(N):
        target.append(dnas[j][i])
    # print(target)
    target.sort() # 사전순 정렬
    dna_cnt=Counter(target)
    # print(dna_cnt)
    mx_cnt=max(dna_cnt.values())
    for dna,cnt in dna_cnt.items():
        if cnt==mx_cnt:
            mn_dna+=dna
            break # 사전순으로 가장 앞서는 것 하나만

print(mn_dna)
ans=0
for i in range(N):
    cnt=0
    for j in range(M):
        if dnas[i][j]!=mn_dna[j]:
            cnt+=1

    ans+=cnt
print(ans)
