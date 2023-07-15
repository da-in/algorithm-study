import sys
n = int(sys.stdin.readline().rstrip("\n"))

for _ in range(n):
    result = 0
    day = int(sys.stdin.readline().rstrip("\n"))
    day_list = list(map(int, sys.stdin.readline().rstrip("\n").split()))

    max_value = -1
    for x in day_list[::-1]:
        if max_value<x:
            max_value = x
        else:
            result += max_value-x
    print(result)