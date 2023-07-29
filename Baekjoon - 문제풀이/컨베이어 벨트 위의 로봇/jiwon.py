import sys
from collections import deque

N,K = map(int, input().split())
belt_list = deque(list(map(int, sys.stdin.readline().split())))
q = deque([0 for _ in range(N)])
x = 0

while belt_list.count(0)<K:
    x+=1
    belt_list.rotate(1)
    q.appendleft(0)
    q.pop()
    q[-1]=0

    for i in range(N-2,-1,-1):
        if q[i]==1 and q[i+1]==0 and belt_list[i+1]>=1:
            q[i]=0
            q[i+1]=1
            q[N-1]=0
            belt_list[i+1]-=1

    if belt_list[0]>=1:
        q[0]=1
        belt_list[0]-=1

print(x)