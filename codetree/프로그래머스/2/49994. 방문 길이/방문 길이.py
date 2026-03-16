def move(di, ci, cj):
    if di=='U':
        ci, cj = ci, cj+1
    elif di=='L':
        ci, cj = ci-1, cj
    elif di=='R':
        ci, cj = ci+1, cj
    else:
        ci, cj = ci, cj-1
    
    return ci, cj
        

def solution(dirs):
    answer = 0
    ci, cj = 0, 0
    v = set()
    for d in dirs:
        nci, ncj = move(d, ci, cj)
        
        if nci<-5 or nci>5 or ncj<-5 or ncj>5:  continue
        
        if (ci, cj, nci, ncj) not in v and (nci, ncj, ci, cj):
            answer+=1
            v.add((ci, cj, nci, ncj))
            v.add((nci, ncj, ci, cj))
        
        ci, cj = nci, ncj
        #print(ci, cj)
    
    return answer