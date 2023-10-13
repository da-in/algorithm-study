import sys
from itertools import combinations

N, M = map(int, input().split())

house, chicken = [], []

for i in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if arr[j] == 1:
            house.append((i, j))
        elif arr[j] == 2:
            chicken.append((i, j))

result = 1e9

for c in combinations(chicken, M):  # M개의 치킨집 조합
    temp = 0
    for h in house:
        dis = 1e9
        for j in range(M):
            dis = min(dis, abs(h[0] - c[j][0]) + abs(h[1] - c[j][1]))
        temp += dis
    result = min(result, temp)

print(result)
