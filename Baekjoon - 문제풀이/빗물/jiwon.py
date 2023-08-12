import sys

H, W = map(int, input().split())
block_list = list(map(int, sys.stdin.readline().split()))

result = 0
for i in range(1, W-1):
    left_max = max(block_list[:i])
    right_max = max(block_list[i+1:])

    min_block = min(left_max, right_max)
    if block_list[i]<min_block:
        result += min_block-block_list[i]

print(result)