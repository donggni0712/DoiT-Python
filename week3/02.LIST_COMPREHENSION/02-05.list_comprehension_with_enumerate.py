list1 = [0, 1, 2, 1, 3, 4, 1]


# list2 = [index for index in range(len(list1)) if list1[index] == 1]
list2 = [index for index, value in enumerate(
    list1) if value == 1]

print(list2)
