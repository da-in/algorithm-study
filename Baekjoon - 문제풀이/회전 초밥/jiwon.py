import sys
# from collections import Counter

# N: 접시 수, d: 초밥 가짓수, k: 연속해서 먹는 접시 수, c: 쿠폰번호
N,d,k,c = map(int, input().split())
sushi_list = [int(sys.stdin.readline()) for _ in range(N)]
max_k = 0

for i in range(N):
    # temp = list(Counter(sushi_list[:k]))
    if i+k>N:
        temp = len(set(sushi_list[i:N] + sushi_list[:(i+k)%N] + [c]))
    else:
        temp = len(set(sushi_list[i:i+k] + [c]))
    max_k = max(temp, max_k)
    if max_k==k+1:
        break
    # sushi_list = sushi_list[1:] + [sushi_list[0]]

print(max_k)