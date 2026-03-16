from itertools import permutations
def is_lucky(s):
    flag = True
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            flag = False # 행운의 문자열 아님 => False
            break

    return flag

S = input()
N = len(S)

targets = set()
for i in permutations(S, N):
    #print(i)
    targets.add(''.join(i)) #서로 다른 문자열

ans = 0
for target in targets:
    cur = is_lucky(target)
    # print(target, n)
    if cur==True:
        ans += 1

# print(targets)
print(ans)