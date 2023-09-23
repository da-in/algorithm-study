import sys

N, S = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))

s,e = 0,0
result = N+1
temp = 0

while(s<=e and e<=N):
    if temp<S:
        if e==N:
            break
        temp+=n_list[e]
        e+=1
    else:
        result = min(result, e-s)
        temp-=n_list[s]
        s+=1

if result == N+1:
    print(0)
else:
    print(result)