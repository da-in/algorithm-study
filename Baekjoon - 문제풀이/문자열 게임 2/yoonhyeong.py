import sys
from collections import defaultdict

T = int(input())

for _ in range(T):
    W = sys.stdin.readline().strip()
    K = int(sys.stdin.readline().strip())

    dic = defaultdict(list)

    for i, ch in enumerate(W): # k번 이상 나온 문자 인덱스 저장
        if W.count(ch) >= K:
            dic[ch].append(i)

    min_result = sys.maxsize
    max_result = 0

    for ch, index_list in dic.items():
        if len(index_list) == K: # 문자의 갯수가 딱 맞을 때
            str_len = index_list[-1] - index_list[0] + 1  # 문자열 길이 구한 뒤,

            min_result = min(min_result, str_len)
            max_result = max(max_result, str_len)

        elif len(index_list) > K:  # 문자의 갯수가 더 많을 때
            for start in range(len(index_list)-K+1):
                end = start + K - 1  # 갯수 K 맞추기

                str_len = index_list[end] - index_list[start] + 1  # 문자열 길이 구하기

                min_result = min(min_result, str_len)
                max_result = max(max_result, str_len)
    if max_result == 0 and min_result == sys.maxsize:
        print(-1)
    else:
        print(min_result, max_result)









