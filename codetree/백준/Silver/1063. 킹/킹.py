def oper_move(order, ci, cj):
    if order == 'R':
        ni, nj = ci+1, cj
    elif order == 'L':
        ni, nj = ci-1, cj
    elif order == 'B':
        ni, nj = ci, cj-1
    elif order == 'T':
        ni, nj = ci, cj+1
    elif order == 'RT':
        ni, nj = ci+1, cj+1
    elif order == 'LT':
        ni, nj = ci-1, cj+1
    elif order == 'RB':
        ni, nj = ci+1, cj-1
    elif order == 'LB':
        ni, nj = ci-1, cj-1
    else:
        ni, nj = -1, -1 # 올바르지 않은 명령

    return ni, nj

col = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
col_rev = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}

king, stone, N = map(str, input().split())
N = int(N)
M = 8
ways = [input().rstrip() for _ in range(N)]

ki, kj = col[king[0]], int(king[1])-1
si, sj = col[stone[0]], int(stone[1])-1
ai, aj = 0, 0
sai, saj = 0, 0
# print(ki,kj)
# print(si,sj)

board = [[0]*M for _ in range(M)]

for way in ways:
    nki, nkj = oper_move(way, ki, kj)
    if nki<0 or nki>=M or nkj<0 or nkj>=M:
        continue

    if (nki, nkj) == (si, sj):
        nsi, nsj = oper_move(way, si, sj)
        if nsi<0 or nsi>=M or nsj<0 or nsj>=M:
            continue
        si, sj = nsi, nsj

    ki, kj = nki, nkj

# print(f'king: {col_rev[ki]}{kj+1} stone: {col_rev[si]}{sj+1}')
print(f'{col_rev[ki]}{kj+1}')
print(f'{col_rev[si]}{sj+1}')
