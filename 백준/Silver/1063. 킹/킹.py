def move(op, i, j):
    if op=='R':
        return i+1, j
    elif op=='L':
        return i-1, j
    elif op=='B':
        return i, j-1
    elif op=='T':
        return i, j+1
    elif op=='RT':
        return i+1, j+1
    elif op=='LT':
        return i-1, j+1
    elif op=='RB':
        return i+1, j-1
    elif op=='LB':
        return i-1, j-1
    else:
        return i, j


col = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
change = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}

king, stone, move_cnt = input().split()
move_cnt = int(move_cnt)
info = [input() for  _ in range(move_cnt)]

# print(king[0], king[1])

ki, kj = col[king[0]], (int(king[1])-1) # 킹 좌표
ti, tj = col[stone[0]], (int(stone[1])-1) # 돌 좌표

for operation in info:
    nki, nkj = move(operation, ki, kj)

    if nki<0 or nki>=8 or nkj<0 or nkj>=8:
        continue

    # print("왕 위치: ", ki, kj)

    if (nki, nkj)==(ti, tj):
        nti, ntj = move(operation, ti, tj)

        # print("현재 돌의 위치: ", ti, tj)

        if nti<0 or nti>=8 or ntj<0 or ntj>=8:
            continue
        ti,tj = nti, ntj
    ki,kj = nki, nkj

    # print("===현재 왕, 돌의 위치===")
    # print(operation, ": ", ki, kj, "/", ti, tj)
    # print("=================")
    # print(f'{change[ki]}{kj+1} {change[ti]}{tj+1}')

print(f'{change[ki]}{kj+1}')
print(f'{change[ti]}{tj+1}')
