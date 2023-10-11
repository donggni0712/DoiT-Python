good_students = [0 for _ in range(31)]

for i in range(28):
    n = int(input())
    good_students[n] = 1

# for i in range(1, 31):
#     if good_students[i] == 0:
#         print(i)

for i, student in enumerate(good_students):
    if student == 0 and i != 0:
        print(i)
