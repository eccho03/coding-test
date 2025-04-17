def solution(skill, skill_trees):
    answer = 0
    tmp = ""
    flag = 0
    
    for i in range(len(skill_trees)):
        target = skill_trees[i]         # 문자열 하나 가져오기
        
        for j in range(len(target)):
            if target[j] not in skill:  continue # 스킬트리와 무관
            tmp += target[j]
            
        if tmp=="":
            answer +=1
        else:
            for k in range(len(tmp)):
                if tmp[k]!=skill[k]:
                    #print(tmp[k])
                    flag = 1
                    break
                else:
                    flag = 0
                    #print(skill[k])

            if flag==0:
                answer += 1
            tmp = ""
            
    return answer