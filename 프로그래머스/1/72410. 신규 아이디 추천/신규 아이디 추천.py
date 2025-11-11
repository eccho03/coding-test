def solution(new_id):
    answer = ''
    
    new_id = new_id.lower()
    # print(new_id)
    target = ['-', '_', '.', '1', '2','3', '4', '5', '6', '7', '8', '9', '0']
    
    tmp_id = ""
    
    for ch in new_id:
        if ch.isalpha() or ch in target:
            tmp_id+=ch
    
    new_id=tmp_id
    # print(new_id)
    
    tmp_id = ""
    flag=False
    for ch in new_id:
        if ch=='.':
            if not flag:
                tmp_id += '.'
            flag = True
        else:
            tmp_id+=ch
            flag=False
                    
    new_id=tmp_id
    # print(new_id)
    
    if len(new_id)>0 and new_id[0]=='.':
            new_id=new_id[1:]
    if len(new_id)>0 and new_id[-1]=='.':
        new_id=new_id[:-1]
    
    if len(new_id)==0:
        new_id='a'
    
    # print(new_id)
    
    if len(new_id)>=16:
        new_id=new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
#     print(new_id)
    
    while len(new_id)<3:
        new_id+=new_id[-1]
    
    return new_id