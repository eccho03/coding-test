def check(letter):
    # L개 선택 - 모두 달라야함
    # 최소 한 개의 모음 / 최소 두 개의 자음
    # 앞에서부터 사전순이어야함
    flag1,flag2=0,0

    # ------------------
    # L개 모두 다른 문자열
    letter_set = set()
    for ch in letter:
        letter_set.add(ch)
    if len(letter_set)==len(letter):
        flag1=1
    # ------------------
    # 최소 한개의 모음/최소 두개의 자음
    moeum, jaeum = 0, 0
    for ch in letter:
        if ch in ('a','e','i','o','u'):
            moeum+=1
        else:
            jaeum+=1

    if moeum>=1 and jaeum>=2:
        flag2=1


    if flag1==1 and flag2==1:
        return True
    else:
        return False

def dfs(idx, cnt, cur):
    # 인덱스/사용개수/현재문자열

    if idx>=C:
        if len(cur)==L and check(cur):
            print(cur)
        return

    #현재문자 선택o
    dfs(idx+1, cnt+1, cur+arr[idx])

    #현재문자 선택x
    dfs(idx+1, cnt, cur)


L, C = map(int, input().split())
arr = list(input().split())
arr.sort()

dfs(0, 0, "")
