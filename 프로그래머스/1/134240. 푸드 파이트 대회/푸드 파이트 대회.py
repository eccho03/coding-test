def solution(food):
    answer = ''
    left = ''
    
    for i in range(1, len(food)):
        #i번째
        #print(food[i]//2)
        left += str(i) * int(food[i]//2)

    right = left[::-1]
    
    return left+'0'+right