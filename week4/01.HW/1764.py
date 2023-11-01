N, M = map(int, input().split(' '))
no_listen_dict = {}
no_look_names = []

for _ in range(N):
    no_listen_name = input().strip()
    no_listen_dict[no_listen_name] = True

for _ in range(M):
    no_look_name = input().strip()
    no_look_names.append(no_look_name)

names = []

for name in no_look_names:
    if name in no_listen_dict:
        names.append(name)

names.sort()

print(len(names))
for x in names:
    print(x)
