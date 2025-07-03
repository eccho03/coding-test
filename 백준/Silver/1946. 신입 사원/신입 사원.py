import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    students = []

    for _ in range(N):
        p1, p2 = map(int, input().split())
        students.append((p1, p2))

    students.sort()

    mn_pass1 = students[0][0] # 서류 - 성적
    cur_mx_pass2 = students[0][1] # 면접 - 순위 (따라서 반대가 큰거임...)
    cnt = 1

    for student in students[1:]:
        std1, std2 = student
        if std2 < cur_mx_pass2:
            cur_mx_pass2 = std2
            cnt += 1

    print(cnt)

'''
핵심 접근은 생각해냄 
(서류 점수 기준 정렬한 다음에 자기보다 서류 점수 높은 학생 중에 
면접 점수도 더 높은 학생 있으면 밀리는 것)
하지만 그렇게 구하려면 O(N**2)라고 착각해서 안 된다 생각했다.
=> tmp 처럼 현재까지 중 가장 큰 값만 저장하는 식으로 하면 무리 없었다.
그리고 서류와 면접이 "등수"가 아닌 "점수"라고 착각했다.
'''