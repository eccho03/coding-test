from collections import deque
def solution(numbers, hand):
    
    answer = ''
    keypad = [['1', '2', '3'],['4', '5', '6'],['7', '8', '9'],['*', '0', '#']]
    
    def find_loc(target):
        for i in range(4):
            for j in range(3):
                if keypad[i][j]==target:
                    return i, j
        return -1,-1
    
    def check_dist(si, sj, ei, ej):
        q = deque()
        v = set()

        q.append((si, sj, 0))
        v.add((si, sj))

        while q:
            ci, cj, dist = q.popleft()

            if (ci, cj)==(ei, ej):
                return dist

            for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                ni, nj = ci+di, cj+dj

                if 0<=ni<4 and 0<=nj<3 and (ni, nj) not in v:
                    q.append((ni, nj, dist+1))
                    v.add((ni, nj))
        return -1
            
    
    li, lj = 3, 0
    ri, rj = 3, 2
    
    for i in range(len(numbers)):
        # print(f'{i}번째: 왼: {li, lj} , 오: {ri, rj}')
        if numbers[i]==1 or numbers[i]==4 or numbers[i]==7:
            answer+='L'
            li, lj = find_loc(str(numbers[i]))
            # print(i, li, lj)
            
        elif numbers[i]==3 or numbers[i]==6 or numbers[i]==9:
            answer+='R'
            ri, rj = find_loc(str(numbers[i]))
            # print(i, ri, rj)
        else:
            ei, ej = find_loc(str(numbers[i])) 
            
            left_dist = check_dist(li, lj, ei, ej)
            right_dist = check_dist(ri, rj, ei, ej)
                        
            if left_dist<right_dist:
                answer+='L'
                li, lj = ei, ej
            elif left_dist>right_dist:
                answer+='R'
                ri, rj = ei, ej
            else:
                if hand=="right":
                    answer+='R'
                    ri, rj = ei, ej
                else:
                    answer+='L'
                    li, lj = ei, ej
            
            # print(i, left_dist, right_dist)
        
        
    
    
    return answer