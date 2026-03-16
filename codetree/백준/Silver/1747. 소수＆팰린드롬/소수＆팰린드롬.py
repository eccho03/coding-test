import math

N = int(input())

def is_prime(N):
    for i in range(2,int(math.sqrt(N))+1):
        if N%i==0:
            #print("소수 아님")
            return False
    return True

def is_palindrome(num):
    for i in range(len(num)):
        if num[i]!=num[len(num)-1-i]:
            return False
    return True

if N==1:
    print(2)
else:
    i=N
    while True:
        num = str(i)
        is_pal = False
        is_sosu = True

        is_sosu = is_prime(i)
        is_pal = is_palindrome(str(i))

        if is_sosu==True and is_pal==True:
            print(i)
            break
        i+=1