def solution(s, n):
    answer = ''
    for cur in s:
        if cur==' ':
            answer+=cur
        elif cur.isalpha():
            if cur.isupper():
                answer+=chr((ord(cur)-ord('A')+n)%26+ord('A'))
            else:
                answer+=chr((ord(cur)-ord('a')+n)%26+ord('a'))

    return answer