R, C, M = map(int, input().split())
shk = []
for _ in range(M):
    r,c,s,d,z = list(map(int, input().split()))
    shk.append([r-1,c-1,s,d,z])

W, H = 2 * C - 2, 2 * R - 2
width = [i for i in range(C)] + [i for i in range(C - 2, 0, -1)]
height = [i for i in range(R)]+[i for i in range(R - 2, 0, -1)]

ans = 0

shk.sort(key=lambda x: (x[1],x[0])) # 열, 행 오름차순 정렬
for j in range(C):
    # 1 상어 잡기
    for i in range(len(shk)):
        if shk[i][1]==j:
            ans+=shk[i][4]
            shk.pop(i)
            break

    #2 상어 이동
    for i in range(len(shk)):
        r, c, s, d, z = shk[i]

        if d == 3 or d == 4:  # 우좌
            dr = 1 if d == 3 else -1  # 우측 -> 더하기
            c = (c + s * dr) % W
            if C <= c:
                c = width[c]  # 좌표 변환
                if d == 3:
                    d = 4
                else:
                    d = 3  # 방향 변환
        else:  # 하상
            dr = 1 if d == 2 else -1  # 하 -> 더하기
            r = (r + s * dr) % H
            if R <= r:
                r = height[r]  # 좌표 변환
                if d == 1:
                    d = 2
                else:
                    d = 1 # 방향 변환

        # 이동된 상어의 정보 갱신
        shk[i] = [r, c, s, d, z]

    #3 상어 정렬 -> 같은 좌표면 삭제
    shk.sort(key=lambda x:(x[1], x[0], -x[4]))
    for i in range(len(shk) - 1, 0, -1):
        if shk[i][:2] == shk[i-1][:2]:
            shk.pop(i)

print(ans)