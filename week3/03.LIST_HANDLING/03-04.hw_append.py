good_students = [0 for _ in range(31)]

for i in range(28):
    n = int(input())
    good_students.append(n)

for i in range(1, 31):
    if i not in good_students:
        print(i)
