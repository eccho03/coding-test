from collections import Counter
def solution(topping):
    answer = 0
    N = len(topping)
    left_cnt = Counter(topping)
    right = set()
    for i in range(N):
        left_cnt[topping[i]]-=1
        if left_cnt[topping[i]]==0:
            del left_cnt[topping[i]]
        right.add(topping[i])
        if len(left_cnt) == len(right):
            answer+=1
        # print(topping[:i], topping[i:])
    return answer