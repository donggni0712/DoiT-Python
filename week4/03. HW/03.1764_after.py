N, M = map(int, input().split(' '))
no_listen_dict = {}  # 수정
no_look_names = []

for _ in range(N):
    name = input()
    no_listen_dict[name] = True  # 수정

for _ in range(M):
    no_look_name = input()
    no_look_names.append(no_look_name)

names = []

for name in no_look_names:
    if name in no_listen_dict:
        names.append(name)

names.sort()

print(len(names))
for x in names:
    print(x)
