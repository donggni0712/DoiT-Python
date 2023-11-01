N, M = map(int, input().split(' '))
no_listen_names = []
no_look_names = []

for _ in range(N):
    name = input()
    no_listen_names.append(name)

for _ in range(M):
    no_look_name = input()
    no_look_names.append(no_look_name)

names = []

for name in no_look_names:
    if name in no_listen_names:
        names.append(name)

names.sort()

print(len(names))
for x in names:
    print(x)
