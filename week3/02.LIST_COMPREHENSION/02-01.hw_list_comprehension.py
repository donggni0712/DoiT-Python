# good_students = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

good_students = [0 for _ in range(31)]

for i in range(28):
    n = int(input())
    good_students[n] = 1

for i in range(1, 31):
    if good_students[i] == 0:
        print(i)
