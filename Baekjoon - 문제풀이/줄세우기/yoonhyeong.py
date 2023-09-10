import sys

N = int(sys.stdin.readline())

d = [1 for _ in range(N)]

num = []
for i in range(N):
    num.append(int(sys.stdin.readline()))

for i in range(N):
    for j in range(i):
        if num[j] < num[i]:
            d[i] = max(d[i], d[j]+1)

print(N - max(d))
