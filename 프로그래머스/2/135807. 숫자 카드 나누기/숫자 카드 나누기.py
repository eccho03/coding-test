import math
def solution(arrayA, arrayB):
    ans_lst = []
    answer = 0
    
    def gcd_list(arr):
        g = arr[0]
        for x in arr[1:]:
            g = math.gcd(g, x)
        return g
    
    def get_divisors(num):
        divs = set()
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                divs.add(i)
                divs.add(num // i)
        return sorted(divs, reverse=True)
    
    mx_mul_A = gcd_list(arrayA)
    mx_mul_B = gcd_list(arrayB)
    mx_muls_A = get_divisors(mx_mul_A)
    mx_muls_B = get_divisors(mx_mul_B)
    
    # print("mula",mx_muls_A)
    # print("mulb",mx_muls_B)
    
    if len(mx_muls_A)!=1:
        for num in mx_muls_A:
            if all(num>=j or j%num!=0 for j in arrayB):
                ans_lst.append(num)
                break
    if len(mx_muls_B)!=1:        
        for num in mx_muls_B:
            if all(num>=j or j%num!=0 for j in arrayA):
                ans_lst.append(num)
                break
    
    if len(ans_lst)==0:
        answer=0
    else:
        answer=max(ans_lst)
    return answer