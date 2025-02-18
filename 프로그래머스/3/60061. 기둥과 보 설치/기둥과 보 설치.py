def menu(func, arch, cur):
    if func == 0:
        #삭제
        if cur in arch:
            arch.remove(cur)
    else:
        #설치
        arch.append(cur)
        
def check_gi(gi, bo):
    for x, y in gi:
        if y == 0:
            continue
        if [x, y - 1] in gi:
            continue
        if [x - 1, y] in bo or [x, y] in bo:
            continue
        return False
    return True

def check_bo(gi, bo):
    for x, y in bo:
        if [x, y - 1] in gi or [x + 1, y - 1] in gi:
            continue
        if [x - 1, y] in bo and [x + 1, y] in bo:
            continue
        return False
    return True

def solution(n, build_frame):
    answer = []
    gi = []
    bo = []
    
    # 형식에 맞춰 저장
    for frame in build_frame:
        x, y, a, b = frame
        cur_frame = [x, y]
        
        if b == 1: #설치
            if a == 0: #기둥
                gi.append(cur_frame)
                if not check_gi(gi, bo):
                    gi.remove(cur_frame)
            else: #보
                bo.append(cur_frame)
                if not check_bo(gi, bo):
                    bo.remove(cur_frame)
        else: #삭제
            tmp = cur_frame
            if a == 0:
                gi.remove(tmp)
            else:
                bo.remove(tmp)

            # 삭제 후에도 구조가 유지되는지 확인
            if not check_gi(gi, bo) or not check_bo(gi, bo):
                # 구조가 깨지면 다시 추가
                if a == 0:
                    gi.append(tmp)
                else:
                    bo.append(tmp)
                    
        answer = [[x, y, 0] for x, y in gi] + [[x, y, 1] for x, y in bo]
        
    return sorted(answer)