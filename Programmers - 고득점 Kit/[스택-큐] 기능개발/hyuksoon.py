def solution(progresses, speeds):
    answer = []
    data=[]
    for i in range(len(progresses)):
        calc=(100-progresses[i])//speeds[i]
        if (100-progresses[i])%speeds[i]!=0:
            calc+=1
        if data and data[-1]>calc:
                data.append(data[-1])
        else:
            data.append(calc)

    
    sum=1
    for i in range(1,len(data)):
        if data[i]!=data[i-1]:
            answer.append(sum)
            sum=1
        else:
            sum+=1
    answer.append(sum)
    return answer
