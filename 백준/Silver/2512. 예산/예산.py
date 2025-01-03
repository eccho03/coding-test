import sys

def binary_search(arr, budget, start, end):
    while start <= end:
        cnt = 0
        mid = (start + end) // 2

        for i in arr:
            if i > mid:
                cnt += mid
            else:
                cnt += i
        
        if cnt > budget:
            end = mid - 1
        else:
            start = mid + 1
        
    return end

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))

budget = int(sys.stdin.readline().rstrip())
res = binary_search(arr, budget, 1, max(arr))
print(res)


