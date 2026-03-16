def binary_search(value):
    left, right = 0, N-1
    target = -1

    while left <= right:
        mid = (left + right) // 2
        if powers[mid] >= value:
            target = mid
            right = mid - 1  # 더 작은 인덱스
        else:
            left = mid + 1

    return target

N,M = map(int,input().split())

names = []
powers = []
for _ in range(N):
    name, power = input().split()
    power = int(power)
    names.append(name)
    powers.append(power)

lst = list(int(input()) for _ in range(M))

for num in lst:
    idx = binary_search(num)
    print(names[idx])