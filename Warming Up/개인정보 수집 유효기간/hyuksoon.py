def solution(today, terms, privacies):
    answer = []
    today=int(today.split('.')[0])*12*28+int(today.split('.')[1])*28+int(today.split('.')[2])
    term={}
    for t in terms:
        temp=t.split(' ')
        term[temp[0]]=int(temp[1])

    for p in range(len(privacies)):
        temp=privacies[p].split(' ')
        t=temp[1]
        time=int(temp[0].split('.')[0])*12*28+int(temp[0].split('.')[1])*28+int(temp[0].split('.')[2])+term[t]*28
        
        if time<=today:
            answer.append(p+1)

    return answer