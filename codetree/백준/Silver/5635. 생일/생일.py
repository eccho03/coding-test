N = int(input())
arr = [list(input().split()) for _ in range(N)]

# 가장 나이가 어린 사람
arr.sort(key=lambda x:(int(x[3]), int(x[2]), int(x[1])), reverse=True)
print(arr[0][0])

# 가장 나이가 많은 사람 (생일 가장 빠름)
# x[1] 일 / x[2] 월 / x[3] 년
arr.sort(key=lambda x:(int(x[3]), int(x[2]), int(x[1])))
print(arr[0][0])