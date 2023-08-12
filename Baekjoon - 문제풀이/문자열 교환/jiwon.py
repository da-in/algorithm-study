from collections import deque

S = list(input())
S_deque = deque(S)

num_a = S.count('a')
answer = len(S)+1

for idx in range(len(S)):
    answer = min(answer, S[0:num_a].count('b'))
    S_deque.rotate(1)
    S = list(S_deque)

print(answer)