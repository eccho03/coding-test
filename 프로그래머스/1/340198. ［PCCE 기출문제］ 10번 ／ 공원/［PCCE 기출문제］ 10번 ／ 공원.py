def solution(mats, park):
    answer = 0
    
    candidate = []
    
    mats.sort(reverse = True)
    
    if len(park)==1 and 1 in mats:
        answer = 1
    else:
    
        for mat in mats:
            for si in range(len(park)-mat+1):
                cur_flag = False
                for sj in range(len(park[0])-mat+1):
                    flag = True
                    for i in range(si, si+mat):
                        for j in range(sj, sj+mat):
                            #print(park[i][j], end=' ')
                            if park[i][j]!='-1':
                                flag = False
                        #print()

                    if flag == True:
                        #print("가능")
                        candidate.append(mat)
                        cur_mat = True
                        break
                    #print()
                if cur_flag == True:
                    break
            # if cur_mat == True:
            #     break
        #print(candidate)
        if len(candidate)==0:
            answer = -1
        else:
            answer = candidate[0]
                
    return answer