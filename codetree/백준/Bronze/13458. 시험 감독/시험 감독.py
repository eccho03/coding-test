n = int(input())
people = list(map(int, input().split()))
b, c = map(int, input().split())

p1 = n
p2 = 0

for i in range(len(people)):
    people[i] -= b
    if people[i] > 0:
        p2 += people[i] // c
        if people[i] % c != 0:
            p2 += 1
print(p1+p2)