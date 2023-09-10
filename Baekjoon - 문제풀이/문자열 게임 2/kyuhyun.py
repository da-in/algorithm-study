from collections import defaultdict
T = int(input())

while T > 0:
    W = input()
    K = int(input())

    res_min = 10000
    res_max = 0
    flag = 0

    str_dic = defaultdict(int)
    idx_dic = defaultdict(list)

    for c in W:
        str_dic[c] += 1

    for i in range(len(W)):
        if str_dic[W[i]] < K:
            continue

        # K개 이상인 경우 모든 인덱스 저장
        idx_dic[W[i]] += [i]
        flag = 1

    for val in idx_dic.values():
        for i in range(len(val)-K+1):
            res_max = max(res_max, (val[i+K-1] - val[i])+1)
            res_min = min(res_min, (val[i+K-1] - val[i])+1)

    if flag == 0:
        print(-1)
    else:
        print(res_min, res_max)
    T -= 1
