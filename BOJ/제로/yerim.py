# 백준 10773번: 제로 (Silver 4)
# https://www.acmicpc.net/problem/10773
# 소요 시간 : 10분

k = int(input())
nums = []
for i in range(k):
    num = int(input())
    if num: # num이 0이 아니면 해당 수를 쓴다
        nums.append(num)
    else: # num이 0이면 최근에 쓴 수를 지운다
        nums.pop()

print(sum(nums))
