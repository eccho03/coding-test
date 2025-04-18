def solution(s):
    answer = 0
    cnt1, cnt2 = 0, 0
    tmp = ""
    copy_s = s

    while len(copy_s) > 0:
        x = copy_s[0]
        cnt1, cnt2 = 0, 0
        tmp = ""

        for i in range(len(copy_s)):
            tmp += copy_s[i]
            if copy_s[i] == x:
                cnt1 += 1
            else:
                cnt2 += 1
            
            if cnt1 == cnt2:
                answer += 1
                copy_s = copy_s[i+1:]
                break
        else:
            answer += 1
            break

    return answer