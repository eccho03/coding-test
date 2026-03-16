def solution(answers):
    answer = []
    st1 = [1, 2, 3, 4, 5]
    st2 = [2, 1, 2, 3, 2, 4, 2, 5]
    st3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    cnt = [0]*3 # 1~3번 학생 정답 맞힌 개수
    for i in range(len(answers)):
        # print(st1[i%len(st1)])
        if answers[i]==st1[i%len(st1)]:
            cnt[0]+=1
        
        if answers[i]==st2[i%len(st2)]:
            cnt[1]+=1
        
        if answers[i]==st3[i%len(st3)]:
            cnt[2]+=1
    
    mx_cnt = max(cnt)
    
    for i in range(3):
        if cnt[i]==mx_cnt:
            answer.append(i+1)
    return answer