from itertools import combinations
from collections import Counter

def solution(weights):
    weights_dict = Counter(weights)
    pairs = combinations(weights_dict.keys(), 2)
    answer = 0
    ratio = [1, 1 / 2, 2 / 1, 2 / 3, 3 / 2, 4 / 3, 3 / 4]
    for a, b in pairs:
        if a / b in ratio:
            answer += weights_dict[a] * weights_dict[b]
    for v in weights_dict.values():
        answer += v * (v - 1) / 2
    return answer
