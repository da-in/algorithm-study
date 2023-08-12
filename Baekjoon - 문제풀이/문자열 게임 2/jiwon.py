import sys
from collections import Counter

T = int(sys.stdin.readline())

for _ in range(T):
    W = str(sys.stdin.readline().rstrip('\n'))
    K = int(sys.stdin.readline())
    W_dict = dict(Counter(W))
    W_dict_idx = dict()

    for i in range(len(W)):
        if W_dict[W[i]]<K:
            continue
        if W[i] not in W_dict_idx:
            W_dict_idx[W[i]]=[]
        W_dict_idx[W[i]].append(i)

    if not W_dict_idx:
        print(-1)
        continue

    max_value = -1
    min_value = len(W)+1

    for key, value in W_dict_idx.items():
        for i in range(len(value)-K+1):
            max_value = max(max_value, value[i+K-1] - value[i] + 1)
            min_value = min(min_value, value[i+K-1] - value[i] + 1)
        
    if max_value==-1 or min_value==len(W)+1:
        print(-1)
    else:
        print(min_value, max_value)