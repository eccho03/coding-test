N, M = map(int,input().split())

S = set(input() for _ in range(N))
targets = [input() for _ in range(M)]
cnt = 0

for target in targets:
    if target in S:
        cnt += 1

print(cnt)