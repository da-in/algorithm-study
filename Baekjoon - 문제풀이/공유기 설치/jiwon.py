import sys

N, C = map(int, sys.stdin.readline().split())
houses = [int(sys.stdin.readline()) for _ in range(N)]
houses.sort()

max_distance = houses[-1]-houses[0]
s,e = 1, max_distance
result = 0

while s<=e:
    cur = houses[0]
    temp = 1
    m = (s+e)//2

    for i in range(1,N):
        if houses[i]-cur >= m:
            cur = houses[i]
            temp+=1
    
    if temp >= C:
        s = m+1
        result = m
    else:
        e = m-1

print(result)