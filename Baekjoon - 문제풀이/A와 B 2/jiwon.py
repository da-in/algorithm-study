# import sys

# s = sys.stdin.readline().rstrip("\n")
# t = sys.stdin.readline().rstrip("\n")

# def solution(S, T):
#     temp = T
#     for idx in range(len(T)-len(S)):
#         if T[len(T)-1-idx]=='A':
#             temp = temp[:-1]
#         else:
#             temp = temp[:-1]
#             temp = temp[::-1]
    
#     if S==temp:
#         return 1
#     else:
#         return 0
    
# if solution(s, t):
#     print(1)
# elif solution(s[::-1], t[::-1]):
#     print(1)
# else:
#     print(0)

import sys

s = sys.stdin.readline().rstrip("\n")
t = sys.stdin.readline().rstrip("\n")
result = 0

def solution(T):
    global result
    if T == s:
        result = 1
        return
    if len(T)<=0:
        return
    
    if T[-1] == 'A':
        solution(T[:-1])
    
    if T[0] == 'B':
        solution(T[1:][::-1])
    
solution(t)
print(result)