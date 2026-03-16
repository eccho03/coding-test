di = [-1, 0, 1, 0] # 상 우 하 좌
dj = [0, 1, 0, -1]

def push_unit(start, dr): # s를 밀고 연쇄 처리
    q = [] # push할 후보를 저장
    v = set() # 이동 기사 번호 저장
    damage = [0]*(N+1) # 각 유닛별 데미지 누적

    q.append(start)
    v.add(start)

    while q:
        data = q.pop(0)
        ci, cj, h, w, k = knight_info[data]

        """큐에 삽입"""
        # 조건 : 1) 명령 받은 방향 진행, 2)벽이 아니면, 3) 겹치는 다른 조각이면
        ni, nj = ci+di[dr], cj+dj[dr]

        for i in range(ni, ni+h):
            for j in range(nj, nj+w):
                if board[i][j] == 2: # 벽인 경우
                     return
                if board[i][j] == 1:
                    damage[data] += 1

        # 겹치는 다른 유닛 있는 경우 큐에 추가
        for idx in knight_info:
            if idx in v: continue # 이미 움직일 대상이면 체크할 필요 x
            ti, tj, th, tw, tk = knight_info[idx]
            if ni <= ti+th-1 and ni+h-1 >= ti and tj <= nj+w-1 and nj <= tj+tw-1:
                q.append(idx)
                v.add(idx)


    damage[start] = 0  # 명령받은 기사는 데미지 없음
    for idx in v:
        ki, kj, h, w, k = knight_info[idx]

        # for i in range(ki, ki+h):
        #     for j in range(kj, kj+w):
        #         test[i][j] = 0

        # 체력보다 더 큰 데미지면 삭제 처리
        if damage[idx] >= k:
            knight_info.pop(idx)
        # 그렇지 않다면 이동
        else:
            ni,nj = ki+di[dr], kj+dj[dr]
            knight_info[idx] = [ni,nj,h,w,k-damage[idx]]

            # for i in range(ni,ni+h):
            #     for j in range(nj,nj+w):
            #         test[i][j] = idx

L, N, Q = map(int, input().split())

# 보드 초기화
board = [[2] * (L + 2)] + [[2] + list(map(int, input().split())) + [2] for _ in range(L)] + [[2] * (L + 2)]

# 기사 정보
knight_info = {}
init_k = [0] * (N + 1)
test = [[0] * (L+2) for _ in range(L+2)]
for m in range(1, N + 1):
    r, c, h, w, k = map(int, input().split())
    knight_info[m] = [r, c, h, w, k]
    init_k[m] = k
    # for i in range(r, r + h):
    #     for j in range(c, c + w):
    #         test[i][j] = m

# 명령 입력
for _ in range(Q):
    idx, dr = map(int, input().split())

    # 존재하는 knight에 대해서만 명령 처리
    if idx in knight_info:
        push_unit(idx, dr) # 명령받은 기사(연쇄적으로 밀기 - 벽이 없는 경우)

# 정답 처리
ans = 0
for idx in knight_info:
    ans += init_k[idx] - knight_info[idx][4]
print(ans)