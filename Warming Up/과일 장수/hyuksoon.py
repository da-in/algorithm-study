def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    idx=m-1
    while idx<len(score):
        answer+=m*score[idx]
        idx+=m
    return answer