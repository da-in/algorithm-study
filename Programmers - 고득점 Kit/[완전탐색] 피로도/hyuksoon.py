from itertools import permutations
def solution(k, dungeons):
    answer = 0
    datas=list(permutations(dungeons,len(dungeons)))
    for data in datas:
        power=k
        ck=True
        for cnt,d in enumerate(data):
            if power<d[0]:
                ck=False
                break
            power-=d[1]
        if ck:
            answer=max(answer,cnt+1)
        else:
            answer=max(answer,cnt)
    return answer
