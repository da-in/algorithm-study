import sys
from collections import deque

N = int(input())

arr = list(map(int, sys.stdin.readline().split(' ')))

arr.sort()

lt = 0
rt = len(arr) - 1

temp = sys.maxsize

l_result = 0
r_result = 0

while lt < rt:
    if abs(arr[lt] + arr[rt]) < abs(temp):
        temp = arr[lt] + arr[rt]
        l_result = arr[lt]
        r_result = arr[rt]

    if arr[lt] + arr[rt] > 0:
        rt -= 1
    elif arr[lt] + arr[rt] < 0:
        lt += 1
    else:
        l_result = arr[lt]
        r_result = arr[rt]
        break

print(l_result, r_result)


