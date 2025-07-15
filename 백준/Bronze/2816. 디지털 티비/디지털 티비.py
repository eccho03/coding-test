def is_channel():
    if channels[0]=="KBS1" and channels[1]=="KBS2":
        return True
    else:
        return False

def oper_1(cursor):
    if cursor<0 or cursor>=N-1:
        return cursor
    print("1", end='')
    cursor += 1
    return cursor

def oper_2(cursor):
    if cursor<1 or cursor>=N:
        return cursor
    print("2", end='')
    cursor -= 1
    return cursor

def oper_3(cursor):
    if cursor<0 or cursor>=N-1:
        return cursor
    print("3", end='')
    channels[cursor], channels[cursor+1] = channels[cursor+1], channels[cursor]
    return cursor+1

def oper_4(cursor):
    if cursor<1 or cursor>=N:
        return cursor
    print("4", end='')
    channels[cursor], channels[cursor-1] = channels[cursor-1], channels[cursor]
    return cursor-1



N = int(input())
channels = [input() for _ in range(N)]
idx = 0 #가장 처음 화살표 첫번째 채널

kbs1_idx = channels.index("KBS1")
while idx<kbs1_idx:
    idx = oper_1(idx)
while idx>kbs1_idx:
    idx = oper_2(idx)
while kbs1_idx > 0:
    idx = oper_4(idx)
    kbs1_idx -= 1

kbs2_idx = channels.index("KBS2")
while idx < kbs2_idx:
    idx = oper_1(idx)
while idx > kbs2_idx:
    idx = oper_2(idx)
while kbs2_idx > 1:
    idx = oper_4(idx)
    kbs2_idx -= 1