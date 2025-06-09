from itertools import permutations

def use_kit(kits):
    muscles = 500
    for i in range(N):
        muscles -= K
        muscles += kits[i]

        # print(muscles)

        if muscles < 500:
            return False

    return True

N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 0

for order in permutations(A, N):
    if use_kit(order):
        ans+=1

print(ans)