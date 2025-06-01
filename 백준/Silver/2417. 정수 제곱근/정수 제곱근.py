N = int(input())

start, end = 0, N

q = 0

while start<=end:
    mid = (start+end)//2

    if mid**2>=N:
        q = mid
        end = mid-1
    else:
        start = mid+1

print(q)