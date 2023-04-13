from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    tangerine_type = defaultdict(int)
    for t in tangerine:
        tangerine_type[t] += 1
    counts = sorted(list(tangerine_type.values()), reverse=True)
    for c in counts:
        k -= c
        answer += 1
        if k <= 0:
            break
    return answer
