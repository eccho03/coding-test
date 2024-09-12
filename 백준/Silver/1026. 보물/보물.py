n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()

result = 0
for i in range(n):
    result += a[i] * b[n - i - 1]

print(result)