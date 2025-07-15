def is_all(height):
    cur_loc = 0
    for loc in locations:
        start = loc-height
        end = loc+height

        if not (start <= cur_loc):
            return False
        cur_loc = end

    if cur_loc >= N:
        return True
    else:
        return False

N = int(input())
M = int(input())
locations = list(map(int, input().split()))

start, end = 1, N #가로등 높이

while start <= end:
    mid = (start+end)//2

    if is_all(mid):
        end = mid-1
    else:
        start = mid+1

print(start)