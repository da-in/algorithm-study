from collections import deque
def solution(tickets):
    answer = ["ICN"]
    
    data={}
    for t in tickets:
        if t[0] in data:
            data[t[0]].append([t[1],False])
        else:
            data[t[0]]=[[t[1],False]]

            
    for d in data:
        data[d].sort()
    def dfs(tar):
        for i in data[tar]:
            if not i[1]:
                answer.append(i[0])
                i[1]=True
                if i[0] in data:
                    dfs(i[0])
                if len(answer)==len(tickets)+1:
                    return answer
                answer.pop()
                i[1]=False

    dfs("ICN")
    return answer

