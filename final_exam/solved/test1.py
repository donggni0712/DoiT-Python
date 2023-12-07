arr = list(map(int, input().split()))


def solution(arr):
    sum = 0
    for x in arr[2:]:
        sum += x
    return sum


print(solution(arr))
