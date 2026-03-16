def solution(s):
    answer = 0
    cnt1,cnt2=0,0
    tmp=""
    while len(s)>0:
        x = s[0]
        
        for i in range(len(s)):
            tmp+=s[i]
            if x==s[i]:
                cnt1+=1
            else:
                cnt2+=1
            if cnt1==cnt2:
                answer+=1
                cnt1,cnt2=0,0
                s=s[i+1:]
                break
        else:
            answer+=1
            break
            
    return answer
