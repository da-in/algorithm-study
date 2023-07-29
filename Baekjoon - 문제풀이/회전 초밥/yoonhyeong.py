import sys
from collections import defaultdict

N, d, k, c = map(int, sys.stdin.readline().split())

sushi = []
for _ in range(N):
    sushi.append(int(sys.stdin.readline()))

start, end = 0, k-1

completed = defaultdict(int)

for i in range(end + 1):
    completed[sushi[i]] += 1

result = 0

completed[c] += 1

while start < N:

    result = max(len(completed), result)

    completed[sushi[start]] -= 1

    if completed[sushi[start]] == 0:
        del completed[sushi[start]]

    start += 1
    end += 1

    completed[sushi[end % N]] += 1

print(result)


# defaultdict : value를 지정하지 않은 key의 value를 0으로 가짐.
# sys.stdin.readline().split() : BufferReader, StringTokenizer 라고 생각하면 될 듯
# len(dic) 은 중복되는 키값을 제외하고 총 길이를 반환