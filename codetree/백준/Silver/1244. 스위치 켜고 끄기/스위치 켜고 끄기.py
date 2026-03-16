N=int(input())  # 스위치 개수
switch = list(map(int,input().split()))
S=int(input()) # 학생 수
order = [list(map(int,input().split())) for _ in range(S)]

opp = {0:1, 1:0}
def oper_men(num, switch):
    for i in range(N):
        if (i+1)%num==0:
            # print(i)
            switch[i] = opp[switch[i]]

def oper_women(num, switch):
    num-=1
    left,right = num-1,num+1

    switch[num]=opp[switch[num]]

    while True:
        if left<0 or right>=N:
            break

        if switch[left]!=switch[right]:
            break
        else:
            switch[left] = opp[switch[left]]
            switch[right] = opp[switch[right]]

            left,right = left-1, right+1


def switch_state():
    for i in range(N):
        print(switch[i], end=" ")
        if (i+1)%20==0:
            print()

for gender, num in order:

    if gender==1:   # 남학생
        oper_men(num, switch)
    else:           # 여학생
        oper_women(num, switch)

switch_state()