N = int(input())
target = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

def binary_search(num):
    start, end = 0, N-1

    while start<=end:
        mid = (start+end)//2
        if num<target[mid]:
            end = mid-1
        elif num>target[mid]:
            start = mid+1
        else:
            return True
    return False

target.sort()
for num in nums:
    flag = binary_search(num)
    print(1 if flag else 0)

# print(target)