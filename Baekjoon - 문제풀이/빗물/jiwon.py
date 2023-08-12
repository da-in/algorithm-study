import sys

H, W = int(input().split())
block_list = list(map(int, sys.stdin.readline().split()))

result = 0
max_block = max(block_list)
for i in range(1, W-1):
    left_max = max(block_list[:i])
    right_max = max(block_list[i+1:])
    result += block_list[i]