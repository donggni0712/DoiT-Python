# 04.solution_like_python.py
N, K = map(int, input().split())

arr = [i for i in range(1, N+1) if N % i == 0]

print(0 if K > len(arr) else arr[K-1])
