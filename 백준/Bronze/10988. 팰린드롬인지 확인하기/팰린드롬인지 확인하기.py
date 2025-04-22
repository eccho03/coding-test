s = input()

front = ""
back = ""

for i in range(len(s)//2):
    front += s[i]

if len(s)%2==0:
    for i in range(len(s)-1, len(s)//2-1,-1):
        back += s[i]
else:
    for i in range(len(s)-1, len(s)//2,-1):
        back += s[i]

if front==back:
    print("1")
else:
    print("0")