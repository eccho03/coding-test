def find_B():
    b_lst = []
    for i in range(N):
        for j in range(N):
            if ground[i][j]=='B':
                b_lst.append([i,j])

    return b_lst

def find_E():
    e_lst = []
    for i in range(N):
        for j in range(N):
            if ground[i][j]=='E':
                e_lst.append([i,j])

    return e_lst

def oper_tree(c_mi, c_mj, c_dir, idx):
    n_mi,n_mj = c_mi+direction[idx][0], c_mj+direction[idx][1]

    # 나무 방향 가로
    if c_dir==0:
        c_mi_1, c_mj_1 = c_mi, c_mj-1
        c_mi_2, c_mj_2 = c_mi, c_mj+1

    # 나무 방향 세로
    else:
        c_mi_1, c_mj_1 = c_mi-1, c_mj
        c_mi_2, c_mj_2 = c_mi+1, c_mj

    n_mi_1, n_mj_1 = c_mi_1 + direction[idx][0], c_mj_1 + direction[idx][1]
    n_mi_2, n_mj_2 = c_mi_2 + direction[idx][0], c_mj_2 + direction[idx][1]

    if 0 <= n_mi_1 < N and 0 <= n_mi_2 < N and 0 <= n_mj_1 < N and 0 <= n_mj_2 < N:
        if ground[n_mi][n_mj] != '1' and ground[n_mi_1][n_mj_1] != '1' and ground[n_mi_2][n_mj_2] != '1':
            return n_mi, n_mj, c_dir

    return -1, -1, -1


def rotate_tree(c_mi, c_mj, c_dir):
    for i in range(c_mi-1, c_mi+2):
        for j in range(c_mj-1, c_mj+2):
            if i<0 or i>=N or j<0 or j>=N or ground[i][j]=='1':
                return -1, -1, -1
    return c_mi, c_mj, 1-c_dir

from collections import deque
def bfs():
    q = deque()
    v = set()

    # 현재 위치 (B) 삽입
    # 가로인 경우
    b_mi, b_mj = b_lst[1][0], b_lst[1][1]
    if b_lst[0][0]==b_lst[2][0]:
        b_dir = 0
    else:
        b_dir = 1
    q.append((b_mi, b_mj, b_dir, 0))
    v.add((b_mi, b_mj, b_dir))

    while q:
        c_mi, c_mj, c_dir, cnt = q.popleft()

        #print(c_mi, c_mj, c_dir, e_lst)

        if (c_mi, c_mj)==(e_mi, e_mj) and c_dir==e_dir:
            return cnt

        for i in range(5):
            if i<4:
                n_mi, n_mj, n_dir = oper_tree(c_mi, c_mj, c_dir, i)
            else:
                n_mi, n_mj, n_dir = rotate_tree(c_mi, c_mj, c_dir)

            if n_mi != -1 and (n_mi, n_mj, n_dir) not in v:
                q.append((n_mi, n_mj, n_dir, cnt + 1))
                v.add((n_mi, n_mj, n_dir))

    return 0


N = int(input())
ground = [list(input()) for _ in range(N)]
direction = [[-1,0],[1,0],[0,-1],[0,1]] # 상, 하, 좌, 우

b_lst = find_B()
e_lst = find_E()
e_mi, e_mj = e_lst[1][0], e_lst[1][1]
if e_lst[0][0] == e_lst[2][0]:
    e_dir = 0
else:
    e_dir = 1

# print(b_lst)
# print(e_lst)

ans = bfs()
print(ans)

#*********TEST*************
# print(b_lst)
# c_lst = oper_U(b_lst)
# print(c_lst)
#**************************