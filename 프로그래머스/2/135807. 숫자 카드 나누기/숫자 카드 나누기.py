import math
def solution(arrayA, arrayB):
    ans_lst = []
    
    # 최대공약수 구하기
    def gcd_list(arr):
        g = arr[0]
        for x in arr[1:]:
            g = math.gcd(g, x)
        return g
    
    mx_mul_A = gcd_list(arrayA)
    mx_mul_B = gcd_list(arrayB)
    
    # print("mula",mx_mul_A)
    # print("mulb",mx_mul_B)
    
    if all(j%mx_mul_A!=0 for j in arrayB):
        ans_lst.append(mx_mul_A)
    if all(j%mx_mul_B!=0 for j in arrayA):
        ans_lst.append(mx_mul_B)

    if len(ans_lst)==0:
        answer=0
    else:
        answer=max(ans_lst)
    return answer