#조건문 ppt 구현해봅시다

score = 90
grade = ''

if score >= 90:
    grade = 'A'
if score >= 80:
    grade = 'B'
if score >= 70:
    grade = 'C'
if score >= 60:
    grade = 'D'
if score < 60:
    grade = 'F'

print("grade: ", grade)

# output
# grade: D
