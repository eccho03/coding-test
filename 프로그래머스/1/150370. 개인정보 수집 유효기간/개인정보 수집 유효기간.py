yakgwan = dict()

def solution(today, terms, privacies):
    answer = []
    
    ty, tm, td = today.split('.')
    ty, tm, td = int(ty), int(tm), int(td)
    #print("today",ty,tm,td)
    
    for term in terms:
        yak, valid = term.split()
        yakgwan[yak] = int(valid)
    
    #print(yakgwan)
    
    for i in range(len(privacies)):
        date, yak = privacies[i].split()
        #print(date, yak, end=' ')
        yy, mm, dd = date.split('.')
        
        valid = yakgwan[yak]
        #print(valid)
        
        
        yy, mm, dd = int(yy), int(mm), int(dd)
        
        #print("before",yy,mm,dd)
        
        #print(valid)
        #print(mm+valid)
        
        if (mm+valid)<=12:
            mm+=valid
        else:
            yy+=(mm+valid)//12
            mm=(mm+valid)%12
            if mm==0:
                mm=12
                yy-=1
            
        if dd-1==0:
            mm-=1
            dd=28
        else:
            dd-=1
        
        #print("after",yy,mm,dd)
        
        if yy>ty or (yy==ty and mm>tm) or (yy==ty and mm==tm and dd>=td):
            pass
        else:
            answer.append(i+1)
        
        
    return answer