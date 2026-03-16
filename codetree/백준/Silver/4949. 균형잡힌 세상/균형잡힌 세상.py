def check(s):
    q = []
    for i in range(len(s)):
        if s[i]=='(' or s[i]=='[':
            q.insert(0, s[i])

        if s[i]==')':
            if q and q[0]=='(':
                q.pop(0)
            else:
                return ['false']
        if s[i]==']':
            if q and q[0]=='[':
                q.pop(0)
            else:
                return ['false']

    return q

while True:
    flag = 0

    target = input()
    #print(target)
    if target == '.':
        break
    q = check(target)

    if len(q)==0:
        print("yes")
    else:
        print("no")