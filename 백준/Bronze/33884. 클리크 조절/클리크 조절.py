N = int(input())
before = [list(map(int, input().split())) for _ in range(N)]
after = [list(map(int, input().split())) for _ in range(N)]

si,sj = min(before)
ei,ej = min(after)

A,B = ei-si,ej-sj
print(A, B)