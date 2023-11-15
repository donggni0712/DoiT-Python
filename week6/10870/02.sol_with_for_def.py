# 02.sol_with_for_def.py

def fibo(n):
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
    return sum


n = int(input())
print(fibo(n))
