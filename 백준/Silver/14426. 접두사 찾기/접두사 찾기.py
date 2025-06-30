def binary_search(prefix):
    start, end = 0, N-1
    while start<=end:
        mid = (start+end)//2

        if question[mid].startswith(prefix):
            return question[mid]
        elif question[mid] < prefix:
            start = mid+1
        else:
            end = mid-1

    return -1

N, M = map(int, input().split())
question = [input() for _ in range(N)]
question.sort()
answer = [input() for _ in range(M)]

total = 0
for ans in answer:
    tmp = binary_search(ans)
    # print(tmp)
    if tmp != -1:
        total+=1

print(total)

