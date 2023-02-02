def solution(n, lost, reserve):
    answer = [1] * n
    intersection = set(lost) & set(reserve)
    lost = list(set(lost) - intersection)
    reserve = list(set(reserve) - intersection)
    for l in lost:
        answer[l - 1] = 0
    for r in reserve:
        if r != 1 and answer[r - 2] == 0:
            answer[r - 2] = 1
            continue
        if r != n and answer[r] == 0:
            answer[r] = 1
    return sum(answer)
