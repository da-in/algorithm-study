
def solution(n,lost,reserve):

    l = len(lost)
    r = len(reserve)
    answer = n-l

    sorted(lost)
    sorted(reserve)

    for i in range(l):
        for j in range(r):
            if lost[i] == reserve[j]:
                lost[i] = reserve[j] = -1
                answer+=1
                break
    
    for i in range(l):
        for j in range(r):
            if lost[i] + 1 == reserve[j] or lost[i]-1 == reserve[j]:
                lost[i]=reserve[j]=-1
                answer+=1
                break

    return answer