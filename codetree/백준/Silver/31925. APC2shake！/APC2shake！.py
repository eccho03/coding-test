N = int(input())
info = [list(input().split()) for _ in range(N)]
ans = []
for i in range(N):
    name, is_jaehak, is_award, mx_score, cur_score = info[i]
    mx_score = int(mx_score)
    cur_score = int(cur_score)

    # 휴학생 제외
    if is_jaehak == "hewhak":
        continue

    # 역대 국제 대학 프밍 수상자 제외
    if is_award == "winner":
        continue

    # 역대 shake! 3위 이내 수상자 제외
    if -1 < mx_score <= 3:
        continue

    ans.append((name, cur_score))

if len(ans)>=10:
    ans.sort(key=lambda x: x[1])
    for i in range(10,len(ans)):
        ans.pop()
ans.sort()

print(len(ans))
for i in range(len(ans)):
    print(ans[i][0])