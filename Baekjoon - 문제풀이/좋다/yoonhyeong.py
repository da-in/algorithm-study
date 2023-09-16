import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

result = 0

for i in range(N):
    target = arr[i]

    start = 0
    end = N - 1

    while start < end:
        tmp = arr[start] + arr[end]

        if tmp < target:
            start += 1
        elif tmp > target:
            end -= 1
        else:
            if start != i and end != i:
                result += 1
                break
            if start == i:
                start += 1
            elif end == i:
                end -= 1

print(result)

