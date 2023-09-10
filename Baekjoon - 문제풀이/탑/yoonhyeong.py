import sys


N = int(input())

towers = list(map(int, sys.stdin.readline().split()))

stack = []

result = [0] * N

for i in range(N):
    while stack:
        if towers[i] > stack[-1][0]:
            stack.pop()
        else:
            result[i] = (stack[-1][1]+1)
            break

    stack.append((towers[i], i))

print(" ".join(map(str, result)))
