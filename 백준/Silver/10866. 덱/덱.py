def push_back(num):
    q.append(num)

def push_front(num):
    q.insert(0, num)

def pop_front():
    if len(q) == 0:
        print(-1)
        return
    print(q.pop(0))

def pop_back():
    if len(q) == 0:
        print(-1)
        return
    print(q.pop())

def size():
    print(len(q))

def is_empty():
    if len(q) == 0:
        print(1)
    else:
        print(0)

def front():
    if len(q) == 0:
        print(-1)
        return
    print(q[0])

def back():
    if len(q) == 0:
        print(-1)
        return
    print(q[-1])

N = int(input())
q = []
num = -1

for _ in range(N):
    parts = input().split()
    operate = parts[0]

    if operate == "push_back" or operate == "push_front":
        num = int(parts[1])

    if operate == "push_back":
        push_back(num)
    elif operate == "push_front":
        push_front(num)
    elif operate == "pop_front":
        pop_front()
    elif operate == "pop_back":
        pop_back()
    elif operate == "size":
        size()
    elif operate == "empty":
        is_empty()
    elif operate == "front":
        front()
    elif operate == "back":
        back()
    else:
        print("command error") # 여기 올 일은 없음

    #print(q)