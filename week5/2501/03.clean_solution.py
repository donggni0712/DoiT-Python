# 03.clean_solution.py
N, K = map(int, input().split())

sum = 0
res = 0

for x in range(1, N+1):
    if N % x == 0:
        sum += 1
    if sum == K:
        res = x
        break
print(res)
