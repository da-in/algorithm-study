def solution(clothes):
    answer = 1
    data={}
    for i in clothes:
        if i[1] in data:
            data[i[1]].append(i[0])
        else:
            data[i[1]]=[i[0]]
    
    c=[]
    for i in data:
        c.append(len(data[i]))
    for i in c:
        answer*=i
    return answer