# 백준 10773번: 제로 (Silver 4)
# https://www.acmicpc.net/problem/10773
# 소요 시간 : 10분

k = int(input())
nums = []
for i in range(k):
    num = int(input())
    if num:
        nums.append(num)
    else:
        nums.pop()

print(sum(nums))
