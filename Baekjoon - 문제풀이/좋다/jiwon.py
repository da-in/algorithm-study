import sys
from itertools import combinations

N = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().rstrip('\n').split()))

n_list.sort()

done = []
result = 0

for i in range(len(n_list)):
    if n_list[i] in done:
        continue

    s = 0
    e = len(n_list)-1

    if s==i:
        s+=1
    if e==i:
        e-=1

    done.append(n_list[i])

    while s<e:
        if n_list[s]+n_list[e] > n_list[i]:
            e-=1
            if e==i:
                e-=1
        elif n_list[s]+n_list[e] < n_list[i]:
            s+=1
            if s==i:
                s+=1
        else:
            c = n_list.count(n_list[i])
            result+=c
            break

print(result)