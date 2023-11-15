# 01.sol_with_for.py

n = int(input())

preprev = 0
prev = 1

sum = 0

for i in range(n+1):
    if i == 0:
        sum = preprev
    elif i == 1:
        sum = prev
    else:
        sum = prev+preprev
        preprev = prev
        prev = sum

print(sum)
