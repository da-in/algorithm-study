def solution(citations):
    max_c = max(citations)
    count = [0] * (max_c + 1)
    for c in citations:
        count[c] += 1

    for i in range(max_c, 0, -1):
        count[i - 1] += count[i]

    for i in range(max_c + 1):
        if count[i] < i:
            return max(0, i - 1)
    return max_c
