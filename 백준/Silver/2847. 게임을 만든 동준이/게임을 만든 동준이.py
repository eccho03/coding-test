N = int(input())
scores = list(int(input()) for _ in range(N))

# print(scores)

cnt = 0
mx_score = scores[-1]
for i in range(N-2, -1, -1):
    #print(scores[i], i, mx_score)
    if scores[i] >= mx_score:
        init_score = scores[i]
        scores[i] = mx_score-1
        mx_score = scores[i]
        cnt += init_score-scores[i]
        # print("mx score",mx_score)
        # print("cnt",cnt)
        # print()
    else:
        mx_score = scores[i]

print(cnt)
#print(scores)