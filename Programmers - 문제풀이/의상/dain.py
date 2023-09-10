from collections import defaultdict

def solution(clothes):
    answer = 1
    type_dict = defaultdict(int)
    for n, t in clothes:
        type_dict[t] += 1
    for c in type_dict.values():
        answer *= c + 1
    return answer - 1
