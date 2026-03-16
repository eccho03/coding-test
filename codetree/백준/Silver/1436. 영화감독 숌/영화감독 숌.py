N = int(input())

ans = 0
cnt = 0

while True:
    if cnt==N:
        print(ans-1)
        break

    if "666" in str(ans):
        # print(ans)
        cnt+=1
    ans+=1
