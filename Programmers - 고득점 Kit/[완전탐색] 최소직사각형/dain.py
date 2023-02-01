def solution(sizes):
    max_w = max_h = 0
    for s in sizes:
        max_w = max(max_w, max(s))
        max_h = max(max_h, min(s))
    return max_w * max_h
