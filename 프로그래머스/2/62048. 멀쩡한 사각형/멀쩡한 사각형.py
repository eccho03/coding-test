import math
def solution(w,h):
    answer = 1
    
    gcd = math.gcd(w,h)
    print(gcd)
    answer = w*h-(w+h-gcd)
    
    return answer