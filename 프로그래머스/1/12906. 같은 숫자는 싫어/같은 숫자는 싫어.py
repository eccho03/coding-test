def solution(arr):
    answer = []
    flag = [0 for _ in range(10)]
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    is_repeat = False
    
    answer.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]:
            is_repeat=True
        if arr[i] not in answer:
            answer.append(arr[i]) #answer에 없으면 무조건 삽입
        elif arr[i] in answer and is_repeat==False:
            answer.append(arr[i])
        is_repeat=False
            
    return answer