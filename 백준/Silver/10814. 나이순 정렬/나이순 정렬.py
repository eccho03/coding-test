import sys

n = int(sys.stdin.readline().rstrip())
people = []
for i in range(n):
    age, person = map(str, sys.stdin.readline().rstrip().split())
    age = int(age)
    people.append([age, person, i])

people.sort(key=lambda x: (x[0], x[2]))

for i in people:
    print(i[0], i[1])