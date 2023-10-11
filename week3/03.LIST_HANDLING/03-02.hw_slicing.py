good_students = [0 for _ in range(31)]

for i in range(28):
    n = int(input())
    good_students[n] = 1

# bad_students = [index for index, value in enumerate(
    # good_students) if value == 0 and index != 0]

bad_students = [index for index, value in enumerate(
    good_students[1:], start=1) if value == 0]

for el in bad_students:
    print(el)
