good_students = [0 for _ in range(31)]

for i in range(28):
    n = int(input())
    good_students[n] = 1

# for i, student in enumerate(good_students):
#     if student == 0 and i != 0:
#         print(i)

bad_students = [index for index, value in enumerate(
    good_students) if value == 0 and index != 0]

for el in bad_students:
    print(el)
