def solution(phone_book):
    answer = True
    
    phone_book.sort()
    
    #print(phone_book)
    
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
        
    return True