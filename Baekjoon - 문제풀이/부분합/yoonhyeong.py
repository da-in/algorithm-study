import sys

N, S = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
tmp = 0

result = sys.maxsize

while True:
    if tmp >= S:
        result = min(result, end - start)
        tmp -= arr[start]
        start += 1

    elif end == N:
        break

    else:
        tmp += arr[end]
        end += 1

if result == sys.maxsize:
    print(0)
else:
    print(result)