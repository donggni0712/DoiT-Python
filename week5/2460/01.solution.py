num = 0

max = 0

for _ in range(10):
    out_people, in_people = map(int, input().split())
    num += in_people
    num -= out_people
    max = num if num > max else max
print(max)
