T = 20

change = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

total = 0
score_total = 0
for _ in range(T):
    subject, score, grade = input().split()
    score = float(score)

    if grade=='P': # 등급이 P인 과목은 계산에서 제외
        continue

    score_total += score
    total += score * change[grade]

print(round(total/score_total, 6))