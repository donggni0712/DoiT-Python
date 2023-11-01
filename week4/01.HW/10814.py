N = int(input())

members = {}

for _ in range(N):
    age, name = input().split()
    if int(age) not in members:
        members[int(age)] = [name]
    else:
        members[int(age)].append(name)

ages = sorted(members.keys())

for age in ages:
    for name in members[age]:
        print(age, name)
