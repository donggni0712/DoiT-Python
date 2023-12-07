n, K = map(int, input().split())


def solution(n):
    if n == 0:
        return K
    if n % 2 == 0:
        return n*solution(n-1)
    return 2*solution(n-1)


print(solution(n))
