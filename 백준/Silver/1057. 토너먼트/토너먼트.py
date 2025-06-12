N, kim, lim = map(int, input().split())

round = 0
while True:
    kim = (kim+1)//2
    lim = (lim+1)//2
    round += 1
    if kim == lim:
        break

print(round)
