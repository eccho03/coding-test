def solution(answers):
    answer = []
    lst = [0 for _ in range(3)]
    
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if answers[i]==num1[i%5]:
            lst[0]+=1
    
    for i in range(len(answers)):
        if answers[i]==num2[i%8]:
            lst[1]+=1
    
    for i in range(len(answers)):
        if answers[i]==num3[i%10]:
            lst[2]+=1
    #print(lst)
    
    mx_score = -1
    for n in range(len(lst)):
        if lst[n] > mx_score:
            mx_score = lst[n]
            answer.clear()
            answer.append(n+1)
        elif lst[n] == mx_score:
            answer.append(n+1)
    answer.sort()
    
    return answer