N = int(input())
pic = dict() # 사진틀
total = int(input())
order = list(map(int, input().split()))

for num in order:

    # 추천받은 학생 사진이 사진틀에 게시

    # 비어있는 사진틀 있을 경우
    if len(pic) < N:
        for n, cnt in pic.items():
            if n==num:
                pic[num] = cnt+1
                break
        else:
            pic[num] = 1

    # 비어있는 사진틀이 없는 경우
    else:

        # 만약 이미 목록에 있으면
        for n, cnt in pic.items():
            if n==num:
                pic[num] = cnt+1
                break
        else:
            # 아니면 하나 빼고 추가
            min_recom = min(pic.values())

            for n, cnt in pic.items():
                if cnt==min_recom:
                    pic.pop(n)
                    break
            pic[num] = 1


    # print(num,": ",pic)

ans = []
for i in pic.keys():
    ans.append(i)

ans.sort()
print(*ans)