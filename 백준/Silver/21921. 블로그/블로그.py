N, X = map(int, input().split())
amounts = list(map(int, input().split()))

num = amounts[:X]
# print(num)
# print(sum(num))
ans = sum(num)
answer = [ans]
for i in range(X, N):
    prev = amounts[i-X]
    ans -= prev
    new = amounts[i]
    ans += new

    # print(ans)
    answer.append(ans)

mx_ans = max(answer)
cnt = 0
for a in answer:
    if a==mx_ans:
        cnt+=1

if mx_ans==0:
    print("SAD")
else:
    print(mx_ans)
    print(cnt)
