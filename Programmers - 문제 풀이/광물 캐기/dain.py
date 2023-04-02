# 그리디
import math


def solution(picks, minerals):
    answer = 0
    div = []
    picks = [1] * picks[2] + [5] * picks[1] + [25] * picks[0]
    mineral_dict = {"diamond": 25, "iron": 5, "stone": 1}
    minerals = list(map(lambda x: mineral_dict[x], minerals))
    minerals = minerals[: len(picks) * 5]
    for i in range(len(minerals) // 5 + 1):
        div.append(minerals[i * 5 : i * 5 + 5])
    div.sort(key=lambda x: (x.count(25), x.count(5), x.count(1)))
    while picks and div:
        p = picks.pop()
        mineral = div.pop()
        for m in mineral:
            answer += math.ceil(m / p)
    return answer


# 시간초과 완전탐색

# from itertools import permutations
# import math
# def solution(picks, minerals):
#     answer = float('inf')
#     mineral_dict = {
#         'diamond':25,
#         'iron':5,
#         'stone':1,
#     }
#     minerals = list(map(lambda x:mineral_dict[x], minerals))
#     picks = [25] * picks[0] + [5] * picks[1] + [1] * picks[2]
#     picks = list(set(permutations(picks)))
#     print(picks)
#     for pick in picks:
#         idx=0
#         cost=0
#         for p in pick:
#             if(idx<len(minerals)):
#                 cost+=sum(map(lambda x: math.ceil(x/p), minerals[idx:idx+5]))
#                 idx+=5
#         answer=min(answer, cost)
#     return answer
