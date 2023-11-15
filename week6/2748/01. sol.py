# 01.sol.py

dp = [-1 for _ in range(91)]


def fibo(n):
    if n <= 1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]


n = int(input())
print(fibo(n))
