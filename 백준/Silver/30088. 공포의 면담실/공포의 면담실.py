N = int(input())
info = [list(map(int, input().split())) for i in range(N)]

info.sort(key=lambda x: (sum(x[1:]))) # 최소 시간 = 부서별로 모든 직원 면담합 작을 때
# print(info)

arr = [0]*N
for i in range(N):
    arr[i] = sum(info[i][1:])
# print(arr)

prefix_arr = [0]*(N+1)
for i in range(N):
    prefix_arr[i+1] = prefix_arr[i] + arr[i]
print(sum(prefix_arr))