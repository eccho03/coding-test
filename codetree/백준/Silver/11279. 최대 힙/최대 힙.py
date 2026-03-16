import heapq

N = int(input())
calculate = [int(input()) for _ in range(N)]

pq = []
for x in calculate:
    if x>0:
        # 배열에 x라는 값 넣기
        heapq.heappush(pq, -x)

    else:
        # 가장 큰 값을 출력하고 배열에서 삭제
        if len(pq)==0:
            print(0)
        else:
            mx_num = -heapq.heappop(pq)
            print(mx_num)