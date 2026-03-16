N, M = map(int, input().split())

alphas = [input().strip() for _ in range(N)]

length = 0
for alpha in alphas:
    length += len(alpha)

cnt = (M-length) // (N-1)
remain = (M-length) % (N-1)

# 대문자/소문자 여부 체크
has_upper = any(a[0].isupper() for a in alphas)
has_lower = any(a[0].islower() for a in alphas)

if has_upper and has_lower:
    flag=3
elif has_upper:
    flag=1
else:
    flag=2

answer = ""

# 대문자 소문자 섞여있는 경우(3)
if flag == 3:
    extra = [0] * (N-1)
    r = remain

    # 1) 다음 단어가 소문자인 간격에 우선 배정
    for i in range(N-1):
        if r>0 and alphas[i + 1][0].islower():
            extra[i] = 1
            r -= 1

    # 2) 남으면 오른쪽부터 아직 안 받은 간격에 배정
    for i in range(N-2, -1, -1):
        if r <= 0:
            break
        if extra[i]==0:
            extra[i]=1
            r -= 1

    # 3) 최종 빌드
    for i in range(N-1):
        answer += alphas[i] + '_' * (cnt+extra[i])
    answer += alphas[N-1]

# 대문자만 있는 경우(1) - 오른쪽부터 배정
elif flag==1:
    extra = [0] * (N-1)
    r = remain
    for i in range(N-2, -1, -1):
        if r <= 0:
            break
        extra[i]=1
        r-=1
    for i in range(N-1):
        answer += alphas[i] + '_' * (cnt+extra[i])
    answer += alphas[N-1]

# 소문자만 있는 경우(2) - 왼쪽부터 배정
elif flag==2:
    extra = [0]*(N-1)
    r = remain
    for i in range(N-1):
        if r <= 0:
            break
        extra[i]=1
        r-=1
    for i in range(N-1):
        answer += alphas[i] + '_' * (cnt+extra[i])
    answer += alphas[N-1]

print(answer)