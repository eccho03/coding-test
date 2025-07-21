def is_full(pic):
    return len(pic)>=N

def delete_pic(reco):
    mn_reco = 1001
    #print(reco)
    for re in reco:
        if 1<=re<mn_reco:
            mn_reco = re

    for pic in pictures:
        if reco[pic] == mn_reco:
            pictures.remove(pic)
            recommends[pic]=0
            return

N = int(input())
recom = int(input())
orders = list(map(int, input().split()))

pictures = []
recommends = [0]*(100+1)

for student in orders:
    if student in pictures:
        recommends[student]+=1
        #print(pictures)
        continue

    if not is_full(pictures):
        pictures.append(student) # 추천받은 학생 게시
    else:
        delete_pic(recommends)
        pictures.append(student)

    recommends[student]+=1
    #print(pictures)

pictures.sort()
print(*pictures)
